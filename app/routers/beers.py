from typing import Optional, Annotated

from fastapi import APIRouter, HTTPException, Depends, status, Header, Response
from sqlalchemy.orm import Session

from app import schemas, crud
from app.dependencies.db import get_db

beers_router = APIRouter(prefix='/beers', tags=['beers'])


@beers_router.post(
    '/', status_code=status.HTTP_201_CREATED, response_model=schemas.BeerReturn
)
def create_beer(
    response: Response, beer: schemas.BeerCreate, db: Session = Depends(get_db)
) -> schemas.BeerReturn:
    result: schemas.BeerReturn = crud.BeerService(db=db, beer=beer).create_beer()
    response.headers['location'] = f'/beers/{result.id}'

    return result


@beers_router.get('/', response_model=list[schemas.BeerReturn])
def get_all_beers(
    db: Session = Depends(get_db), x_max_size: Annotated[int | None, Header()] = 30
) -> list[schemas.BeerReturn]:
    return crud.BeerService.get_all_beers(db=db, limit=x_max_size)


@beers_router.get('/{beer_id}', response_model=schemas.BeerReturn)
def get_beer_with_id(
    beer_id: int, db: Session = Depends(get_db)
) -> schemas.BeerReturn:

    result: Optional[schemas.BeerReturn] = crud.BeerService.get_beer_with_id(
        db=db, beer_id=beer_id
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'beer with id: {beer_id} does not exist',
        )
    return result


@beers_router.patch('/{beer_id}', response_model=schemas.BeerReturn)
def update_beer(beer: schemas.BeerUpdate, beer_id: int, db: Session = Depends(get_db)):
    beer.id = beer_id
    result = crud.BeerService(db=db, beer=beer).update_beer()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'beer with id: {beer_id} does not exist',
        )
    return result


@beers_router.delete('/{beer_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_beer(beer_id: int, db: Session = Depends(get_db)) -> None:
    if not crud.BeerService.get_beer_with_id(db=db, beer_id=beer_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'beer with id: {beer_id} does not exist',
        )
    else:
        crud.BeerService.delete_beer(db=db, beer_id=beer_id)
