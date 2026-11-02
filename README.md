# About this project

This is my third Python project. It is a package for managing a media library containing music, images and videos. Media items are described using dataclasses and stored in a catalog.

## Prerequisites

* Python 3.12 or newer
* uv
* pytest for tests
* pre-commit for code checks

Install the project and its dependencies from the project directory:

```bash
uv sync
```

## How to use it

The package is used through Python imports.

Create a media item and add it to a catalog:

```python
from catalog.catalog import Catalog
from catalog.models import Category, MediaItem

catalog = Catalog()

item = MediaItem(
    id="1",
    name="Chippin' In",
    category=Category.MUSIC,
    year=2019,
    size=5_000_000,
    author="SAMURAI",
)

catalog.add(item)
```

### Examples

Get a media item by its ID:

```python
item = catalog.get("1")
print(item.name)
```

Remove a media item:

```python
catalog.remove("1")
```

### Media item limits

Each media item contains an ID, name, category, year, size and author.

Available categories:

* Music: `Category.MUSIC`
* Images: `Category.IMAGE`
* Videos: `Category.VIDEO`

Names and authors cannot be empty. The year must be between 1900 and the current year. Size is measured in bytes and must be a positive integer.

Duplicate IDs are not allowed. Getting or removing an item with an unknown ID raises `MediaItemNotFound`. Adding an item with an existing ID raises `IDDuplicate`. Invalid media item fields raise `WrongEntity`.

## Tests

Run all tests:

```bash
uv run python -m pytest -v
```

Run code checks:

```bash
uv run pre-commit run --all-files
```

### Few words about the catalog and validation

MediaItem uses a dataclass to describe media objects. Fields are validated in __post_init__ when an object is created.

The catalog stores objects in a dictionary with IDs as keys. Each catalog has its own dictionary. Custom exceptions inherit from CatalogError.
