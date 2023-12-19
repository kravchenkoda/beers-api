from datetime import timedelta, datetime
from typing import Annotated, Optional, Type
from os import environ

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.schemas import User, Token
from app.db_models.users import Users
from app.dependencies.users_db import get_db

db_dependency = Annotated[Session, Depends(get_db)]
auth = APIRouter(prefix='/auth', tags=['auth'])

SECRET_KEY = environ['JWT_SECRET_KEY']
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oath2_bearer = HTTPBearer()


def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(oath2_bearer)]
) -> dict[str, str | int]:
    """
    Get the current user based on the provided OAuth2 token.

    Args:
        token (HTTPAuthorizationCredentials):
            OAuth2 token provided in the request header.

    Returns:
        dict[str, str | int]: User information containing 'username' and 'id'.

    Raises:
        HTTPException: If the user cannot be validated or the token is invalid.
    """
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user'
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if not username or not user_id:
            raise unauthorized
        return {'username': username, 'id': user_id}
    except JWTError:
        raise unauthorized


def authenticate_user(
    username: str, password: str, db: Session
) -> Optional[Type[Users]]:
    """
    Authenticate a user based on the provided username and password.

    Args:
        username (str): User's username.
        password (str): User's password.
        db (Session): SQLAlchemy database session.

    Returns:
        Optional[Type[Users]]: The authenticated user or None if authentication fails.
    """
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return None
    if not bcrypt_context.verify(password, user.hashed_password):
        return None
    return user


def create_access_token(username: str, user_id: int, expires: timedelta):
    """
    Create an access token for the given username and user ID.

    Args:
        username (str): User's username.
        user_id (int): User's ID.
        expires (timedelta): Token expiration time.

    Returns:
        str: The generated access token.
    """
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@auth.post('/', status_code=status.HTTP_201_CREATED)
def create_user(db: db_dependency, user: User):
    user = Users(
        username=user.username, hashed_password=bcrypt_context.hash(user.password)
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        return HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'user with username "{user.username}" already exists',
        )


@auth.post('/token', response_model=Token)
def get_token(form_data: User, db: db_dependency):
    user: Type[Users] = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = create_access_token(user.username, user.id, timedelta(minutes=5))
    return {'access_token': token, 'token_type': 'bearer'}
