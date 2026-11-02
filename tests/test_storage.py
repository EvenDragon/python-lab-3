import json

import pytest

from catalog.catalog import Catalog
from catalog.errors import DamagedFile, UnsupportedFormatVersion
from catalog.models import Category
from catalog.storage import load_json, save_json

from .test_catalog import get_default_item


def test_json_round_trip(tmp_path):
    catalog = Catalog()
    item1, item2 = get_default_item(1, Category.IMAGE), get_default_item(2)
    catalog.add(item1)
    catalog.add(item2)
    path = tmp_path / "catalog.json"
    save_json(catalog, path)
    loaded = load_json(path)
    assert catalog.get("2").id == loaded.get("2").id == "2"

def test_damaged_file(tmp_path):
    catalog = Catalog()
    path = tmp_path / "catalog.json"
    data = {
    "format_version": 1,
    "hmmm":"mmm"
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with pytest.raises(DamagedFile):
        catalog = load_json(path)

    assert catalog.__len__() == 0   #Checks that there is no partial changes

def test_unknown_format_version(tmp_path):
    path = tmp_path / "catalog.json"
    data = {
        "format_version": 2,
        "items": []
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with pytest.raises(UnsupportedFormatVersion):
        load_json(path)
