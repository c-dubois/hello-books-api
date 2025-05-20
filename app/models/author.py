from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    @classmethod
    def from_dict(cls, author_data):
        new_author = cls(title=author_data["name"])
        return new_author
    
    def to_dict(self):
        author_as_dict = dict(id=self.id, name=self.name)
        return author_as_dict