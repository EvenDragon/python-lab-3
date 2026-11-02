import json
from dataclasses import asdict
from pathlib import Path

from catalog.catalog import Catalog
from catalog.constants import FORMAT_VERSION
from catalog.errors import (
    DamagedFile,
    IDDuplicate,
    UnsupportedFormatVersion,
    WrongEntity,
)
from catalog.models import Category, MediaItem


def save_json(catalog: Catalog, path: Path) -> None:
    """Save catalog to json file"""
    items = []

    for item in catalog:
        item_data = asdict(item)
        item_data["category"] = item.category.value
        items.append(item_data)
    data = {
        "format_version": FORMAT_VERSION,
        "items": items
    }

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False,indent=4)

def load_json(path: Path) -> Catalog:
    """Load catalog from json file"""
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise DamagedFile("Invalid json file")

    if not isinstance(data, dict):
        raise DamagedFile("File is not a dict")

    if "format_version" not in data:
        raise UnsupportedFormatVersion("There is no format version in file")

    if data["format_version"] != FORMAT_VERSION:
        raise UnsupportedFormatVersion(f"Wrong format version {data['format_version']}. Use version {FORMAT_VERSION}")

    if "items" not in data:
        raise DamagedFile("There is no items in file")

    catalog = Catalog()

    for i, item_data in enumerate(data["items"]):
        if not isinstance(item_data, dict):
            raise DamagedFile(f"Item at index {i} must be an object")

        try:
            fields = item_data.copy()
            fields["category"] = Category(fields["category"])
            item = MediaItem(**fields)
            catalog.add(item)
        except (
                KeyError,
                TypeError,
                ValueError,
                WrongEntity,
                IDDuplicate,
        ) as e:
            raise DamagedFile(
                f"Invalid media item at index {i}"
            ) from e

    return catalog
