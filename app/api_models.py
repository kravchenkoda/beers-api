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


class BeerSearch(BaseModel):
    id: Optional[int] = None
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


class BeerCreate(BeerBase):
    pass
