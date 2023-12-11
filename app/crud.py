from typing import Type, Optional

from sqlalchemy import update
from sqlalchemy.orm import Session

import db_models
import api_models


class BeerService:
    def __init__(
        self,
        db: Session,
        beer: api_models.BeerCreate | api_models.BeerSearch | api_models.BeerUpdate,
    ):
        """
        Initialize a BeerService instance.

        Args:
            db (Session): SQLAlchemy database session.
            beer (api_models.BeerCreate | api_models.BeerSearch): Beer data.
        """
        self.db = db
        self.beer = beer

    def create_beer(self) -> None:
        """Create a new beer entry in the database."""

        beers_foreign_keys: dict[str, int] = self._get_beers_foreign_keys()
        beer_attributes: dict[str, float | int | str] = beers_foreign_keys
        beer_attributes['abv']: float = self.beer.abv
        beer_attributes['ibu']: int = self.beer.ibu
        beer_attributes['ounces']: float = self.beer.ounces

        self._create_item(
            db_models.Beer, item_name=self.beer.name, other_attrs=beers_foreign_keys
        )

    def update_beer(self):
        """Update a beer in the database."""
        if not (
            self.db.query(db_models.Beer)
            .filter(db_models.Beer.id == self.beer.id)
            .first()
        ):
            return None

        db_update_data = self._prepare_db_update_data()
        self._update_breweries_tables(db_update_data)

        db_update_data.pop('city_id', None)
        db_update_data.pop('state_id', None)
        db_update_data.pop('id', None)
        if db_update_data:
            self._update_item(
                table=db_models.Beer, item_id=self.beer.id, update_items=db_update_data
            )

    def get_beer_with_id(self) -> Optional[api_models.BeerReturn]:
        """
        Retrieve beer details by its ID.

        Returns:
            If beer has been found:
                api_models.BeerReturn: object representing the beer details.
            If beer has not been found:
                None
        """
        beer_found: Optional[db_models.Beer] = (
            self.db.query(db_models.Beer)
            .filter(db_models.Beer.id == self.beer.id)
            .join(db_models.Style)
            .join(db_models.Brewery)
            .first()
        )
        if beer_found:
            return api_models.BeerReturn(
                id=beer_found.id,
                name=beer_found.name,
                ibu=beer_found.ibu,
                abv=beer_found.abv,
                ounces=beer_found.ounces,
                style=beer_found.style.name,
                brewery=beer_found.brewery.name,
                city=beer_found.brewery.city.name,
                state=beer_found.brewery.city.state.name,
            )
        return None

    def _update_item(
        self,
        item_id: int,
        table: Type[db_models.State]
        | Type[db_models.City]
        | Type[db_models.Brewery]
        | Type[db_models.Style]
        | Type[db_models.Beer],
        update_items: dict[str, str | int | float],
    ):
        q = update(table).where(table.id == item_id).values(**update_items)
        self.db.execute(q)
        self.db.commit()

    def _prepare_db_update_data(self):
        db_update_data = {}

        attributes_to_update = {k: v for k, v in self.beer.model_dump().items() if v}

        for attr, value in attributes_to_update.items():
            if attr == 'style':
                style_id: int = self._get_name_corresponding_id(
                    table=db_models.Style, item_name=self.beer.style
                )
                db_update_data['style_id'] = style_id

            elif attr == 'state':
                state_id: int = self._get_name_corresponding_id(
                    table=db_models.State, item_name=self.beer.state
                )
                db_update_data['state_id'] = state_id

            elif attr == 'city':
                self._create_item(
                    table=db_models.City,
                    item_name=self.beer.city,
                    other_attrs={'state_id': db_update_data.get('state_id')},
                )
                city_id = (
                    self.db.query(db_models.City.id)
                    .filter(db_models.City.name == self.beer.city)
                    .all()[-1][0]
                )
                db_update_data['city_id'] = city_id

            elif attr == 'brewery':
                city_id = db_update_data.get('city_id')

                brewery_id = self._get_name_corresponding_id(
                    table=db_models.Brewery,
                    item_name=self.beer.brewery,
                    other_attrs={'city_id': city_id},
                )
                db_update_data['brewery_id'] = brewery_id

            else:
                db_update_data[attr] = value

        return db_update_data

    def _update_breweries_tables(self, db_update_data):
        current_beer_data: api_models.BeerReturn = self.get_beer_with_id()

        city_present: Optional[int] = db_update_data.get('city_id')
        only_state_present: Optional[int] = db_update_data.get(
            'state_id'
        ) and not db_update_data.get('city_id')
        brewery_present: Optional[int] = db_update_data.get('brewery_id')

        if only_state_present:
            if brewery_present:
                brewery_id: int = db_update_data['brewery_id']

            else:
                brewery_id: int = self._get_name_corresponding_id(
                    table=db_models.Brewery, item_name=current_beer_data.brewery
                )

            self._create_item(
                table=db_models.City,
                item_name=current_beer_data.city,
                other_attrs={'state_id': db_update_data['state_id']},
            )
            city_id: int = (
                self.db.query(db_models.City.id)
                .filter(db_models.City.name == current_beer_data.city)
                .all()[-1][0]
            )
            self._update_item(
                table=db_models.Brewery,
                item_id=brewery_id,
                update_items={'city_id': city_id},
            )

        elif city_present:
            if brewery_present:
                brewery_id = db_update_data['brewery_id']

            else:
                brewery_id: int = self._get_name_corresponding_id(
                    table=db_models.Brewery, item_name=current_beer_data.brewery
                )
            self._update_item(
                table=db_models.Brewery,
                item_id=brewery_id,
                update_items={'city_id': db_update_data['city_id']},
            )

    def _get_beers_foreign_keys(self) -> dict[str, int]:
        result = {
            'state_id': self._get_name_corresponding_id(
                db_models.State, self.beer.state
            ),
        }

        related_items = {
            'city_id': (db_models.City, self.beer.city),
            'style_id': (db_models.Style, self.beer.style),
            'brewery_id': (db_models.Brewery, self.beer.brewery),
        }

        for column_name, search_data in related_items.items():
            table, item_name = search_data

            if column_name == 'city_id':
                city_id = self._get_name_corresponding_id(
                    table=table,
                    item_name=item_name,
                    other_attrs={
                        'state_id': self._get_name_corresponding_id(
                            table=db_models.State, item_name=self.beer.state
                        )
                    },
                )
                result[column_name] = city_id

            elif column_name == 'brewery_id':
                brewery_id = self._get_name_corresponding_id(
                    table=table,
                    item_name=item_name,
                    other_attrs={'city_id': result['city_id']},
                )
                result[column_name] = brewery_id

            else:
                result[column_name] = self._get_name_corresponding_id(
                    table=table,
                    item_name=item_name,
                )
        del result['state_id']
        del result['city_id']

        return result

    def _get_name_corresponding_id(
        self,
        table: Type[db_models.State]
        | Type[db_models.City]
        | Type[db_models.Brewery]
        | Type[db_models.Style],
        item_name: str,
        other_attrs: dict[str, str | int | float] = None,
    ) -> Optional[int]:
        result: db_models.Style | db_models.City | db_models.Brewery | None = (
            self.db.query(table.id).filter(table.name == item_name).first()
        )
        if result:
            return result.id
        else:
            if other_attrs:
                self._create_item(table, item_name, other_attrs)
            else:
                self._create_item(table, item_name)

        return self.db.query(table.id).filter(table.name == item_name).first().id

    def _create_item(
        self,
        table: Type[db_models.City]
        | Type[db_models.Brewery]
        | Type[db_models.Style]
        | Type[db_models.Beer],
        item_name: str,
        other_attrs: dict[str, str | int | float] = None,
    ) -> None:
        item = table
        if other_attrs:
            self.db.add(item(name=item_name, **other_attrs))
        else:
            self.db.add(item(name=item_name))
        self.db.commit()
