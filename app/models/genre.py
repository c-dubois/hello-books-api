from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .book import Book

class Genre(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    @classmethod
    def from_dict(cls, genre_data):
        new_genre = cls(name=genre_data["name"])
        return new_genre

    def to_dict(self):
        genre_as_dict = {}
        genre_as_dict["id"] = self.id
        genre_as_dict["name"] = self.name

        return genre_as_dict
