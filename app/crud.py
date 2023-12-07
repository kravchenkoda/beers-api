from typing import Type, Optional

from sqlalchemy.orm import Session

import db_models
import api_models


class BeerService:
    def __init__(
        self, db: Session, beer: api_models.BeerCreate | api_models.BeerSearch
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

    def get_beer_with_id(self) -> Optional[api_models.BeerReturn]:
        """
        Retrieve beer details by its ID.

        Returns:
            If beer has been found:
                api_models.BeerReturn: object representing the beer details.
            If beer has not been found:
                None
        """
        beer_found: db_models.Beer = (
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

            id = self._get_name_corresponding_id(table, item_name)

            if not id:
                if column_name == 'city_id':
                    self._create_item(
                        table, item_name, other_attrs={'state_id': result['state_id']}
                    )
                elif column_name == 'brewery_id':
                    self._create_item(
                        table, item_name, other_attrs={'city_id': result['city_id']}
                    )
                else:
                    self._create_item(table, item_name)
            result[column_name] = self._get_name_corresponding_id(table, item_name)
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
    ) -> Optional[int]:
        result: db_models.Style | db_models.City | db_models.Brewery | None = (
            self.db.query(table.id).filter(table.name == item_name).first()
        )
        if result:
            return result.id
        else:
            return None

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
