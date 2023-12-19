from pydantic import BaseModel
from typing import Optional


class BeerBase(BaseModel):
    name: str
    ibu: int
    abv: float
    ounces: float
    style: str
    brewery: str
    state: str
    city: str


class BeerUpdate(BaseModel):
    name: Optional[str] = None
    ibu: Optional[int] = None
    abv: Optional[float] = None
    ounces: Optional[float] = None
    style: Optional[str] = None
    brewery: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None


class BeerReturn(BeerBase):
    id: int
    city: Optional[str] = None
    state: Optional[str] = None


class BeerCreate(BeerBase):
    pass


class BeerDelete(BaseModel):
    id: int


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
