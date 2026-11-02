from dataclasses import dataclass
from enum import Enum

from catalog.constants import MAX_YEAR, MIN_YEAR
from catalog.errors import WrongEntity


class Category(Enum):
    MUSIC = "Music"
    IMAGE = "Image"
    VIDEO = "Video"


@dataclass
class MediaItem:
    id: str
    name: str
    category: Category
    year: int
    size: int   #in bytes
    author: str

    def __post_init__(self):
        """Validate media item fields"""
        if type(self.id) is not str:
            raise WrongEntity("Media item id must be a string")
        if self.id.strip() == "":
            raise WrongEntity("Media item id cannot be an empty string")

        if type(self.name) is not str:
            raise WrongEntity("Media item name must be a string")
        if self.name.strip() == "":
            raise WrongEntity("Media item name cannot be an empty string")

        if not isinstance(self.category, Category):
            raise WrongEntity(f"Media item category must be one of {Category.__members__}")

        if type(self.year) is not int:
            raise WrongEntity("Media item year must be an integer")
        if not( MIN_YEAR <= self.year <= MAX_YEAR):
            raise WrongEntity("Media item year lies beyond what is accessible to humanity ;)")

        if type(self.size) is not int:
            raise WrongEntity("Media item size must be an integer")
        if self.size <= 0:
            raise WrongEntity("Media item size cannot be less than zero")

        if type(self.author) is not str:
            raise WrongEntity("Media item author must be a string")
        if self.author.strip() == "":
            raise WrongEntity("Media item author cannot be an empty string")
