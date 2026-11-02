from collections.abc import Iterator

from catalog.errors import IDDuplicate, MediaItemNotFound
from catalog.models import Category, MediaItem


class Catalog:
    """Catalog class. Contains dictionary of media items and methods to work with them"""
    def __init__(self):
        self._items: dict[str, MediaItem] = {}

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[MediaItem]:
        """Iterates in order of added items"""
        return iter(self._items.values())

    def __contains__(self, id: str) -> bool:
        return id in self._items

    def add(self, item: MediaItem) -> None:
        """Adds media item to catalog"""
        if self._items.__contains__(item.id):
            raise IDDuplicate(f"Media item with id {item.id} already exists")
        self._items[item.id] = item

    def get(self, id: str) -> MediaItem:
        """Gets media item by id"""
        if id not in self._items:
            raise MediaItemNotFound(f"Media item with id {id} not found")
        return self._items[id]

    def remove(self, id: str) -> None:
        """Removes media item by id"""
        if id not in self._items:
            raise MediaItemNotFound(f"Could't remove media item with id {id}, because it hasn't been found")
        self._items.pop(id)

    def find_by_category(self, category: Category) -> list[MediaItem]:
        """Return all media items belonging to a given category"""
        return [item for item in self._items.values() if item.category == category]

    def find_by_name(self, name: str) -> list[MediaItem]:
        """Return all media items with given name"""
        return [item for item in self._items.values() if item.name.capitalize() == name.capitalize()]
