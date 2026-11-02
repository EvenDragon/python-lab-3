from catalog.errors import IDDuplicate, MediaItemNotFound

from catalog.models import MediaItem


class Catalog:
    """Catalog class. Contains dictionary of media items and methods to work with them"""
    def __init__(self):
        self._items: dict[int, MediaItem] = {}

    def add(self, item: MediaItem) -> None:
        """Adds media item to catalog"""
        if self._items.__contains__(item.id):
            raise IDDuplicate(f"Media item with id {item.id} already exists")
        self._items[item.id] = item

    def get(self, id: int) -> MediaItem:
        """Gets media item by id"""
        if id not in self._items:
            raise MediaItemNotFound(f"Media item with id {id} not found")
        return self._items[id]

    def remove(self, id: int) -> None:
        """Removes media item by id"""
        if id not in self._items:
            raise MediaItemNotFound(f"Could't remove media item with id {id}, because it hasn't been found")
        self._items.pop(id)
