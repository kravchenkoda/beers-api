from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, NUMERIC, VARCHAR

from db import Base


class Style(Base):
    __tablename__ = 'styles'
    __table_args__ = {'keep_existing': True}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    beers: Mapped[list['Beer']] = relationship(back_populates='style')


class State(Base):
    __tablename__ = 'states'
    __table_args__ = {'keep_existing': True}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cities: Mapped[list['City']] = relationship(back_populates='state')


class City(Base):
    __tablename__ = 'cities'
    __table_args__ = {'keep_existing': True}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey('states.id'))
    state: Mapped['State'] = relationship(back_populates='cities')
    breweries: Mapped[list['Brewery']] = relationship(back_populates='city')


class Brewery(Base):
    __tablename__ = 'breweries'
    __table_args__ = {'keep_existing': True}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    city: Mapped['City'] = relationship(back_populates='breweries')
    beers: Mapped[list['Beer']] = relationship(back_populates='brewery')


class Beer(Base):
    __tablename__ = 'beers'
    __table_args__ = {'keep_existing': True}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    ibu: Mapped[int] = mapped_column(Integer(), nullable=False)
    abv: Mapped[float] = mapped_column(NUMERIC(4, 1), nullable=False)
    ounces: Mapped[float] = mapped_column(NUMERIC(4, 1), nullable=False)
    style_id: Mapped[int] = mapped_column(ForeignKey('styles.id'), nullable=False)
    brewery_id: Mapped[int] = mapped_column(ForeignKey('breweries.id'), nullable=False)
    style: Mapped['Style'] = relationship(back_populates='beers')
    brewery: Mapped['Brewery'] = relationship(back_populates='beers')
