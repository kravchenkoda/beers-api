from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import VARCHAR, Integer

UsersBase = declarative_base()


class Users(UsersBase):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(VARCHAR(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(VARCHAR(100))
