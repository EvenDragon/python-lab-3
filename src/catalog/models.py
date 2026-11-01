from dataclasses import dataclass
from catalog.errors import WrongEntity
from catalog.constants import MIN_YEAR, MAX_YEAR

@dataclass
class MediaItem:
    id: int
    name: str
    category: str
    year: int
    size: int
    author: str

    def __post_init__(self):
        """Validate media item fields"""
        if type(self.id) is not int:
            raise WrongEntity("Media item id must be an integer")

        if type(self.name) is not str:
            raise WrongEntity("Media item name must be a string")
        if self.name.strip() == "":
            raise WrongEntity("Media item name cannot be an empty string")

        if type(self.category) is not str:
            raise WrongEntity("Media item category must be a string")
        if self.category.strip() == "":
            raise WrongEntity("Media item category cannot be an empty string")

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
