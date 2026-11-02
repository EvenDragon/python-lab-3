import pytest

from catalog.catalog import Catalog
from catalog.errors import IDDuplicate, MediaItemNotFound
from catalog.models import Category, MediaItem


def get_default_item(id:int, category:Category | None = None) -> MediaItem:
    """Generate a default media item whith a given id"""
    item = MediaItem(
        id=str(id),
        name=f"Video{id}",
        category=category or Category.VIDEO,
        year=2026,
        size=300500,
        author="UNKNOWN"
    )
    return item

def test_add_get():
    catalog = Catalog()
    item = get_default_item(1)
    catalog.add(item)
    assert item.id == catalog.get("1").id

def test_remove():
    catalog = Catalog()
    item = get_default_item(50)
    catalog.add(item)
    catalog.remove(item.id)
    with pytest.raises(MediaItemNotFound):
        catalog.get(item.id)

def test_duplicate_id():
    catalog = Catalog()
    item1 = get_default_item(1)
    item2 = get_default_item(1)
    item2.name = "Video2"
    catalog.add(item1)
    with pytest.raises(IDDuplicate):
        catalog.add(item2)

def test_caterory_search():
    catalog = Catalog()
    item1, item2 = get_default_item(1,Category.MUSIC), get_default_item(2,Category.MUSIC)
    item3 = get_default_item(3,Category.IMAGE)
    catalog.add(item1)
    catalog.add(item2)
    catalog.add(item3)
    result = catalog.find_by_category(Category.MUSIC)
    assert result[0].id == "1" and result[1].id == "2"

def test_name_search():
    catalog = Catalog()
    item1, item2 = get_default_item(1), get_default_item(2)
    catalog.add(item1)
    catalog.add(item2)
    item1.name = "qWertY"
    assert catalog.find_by_name("QWErty")[0].name == item1.name

def test_iteraion_order():
    catalog = Catalog()
    item1,item2,item3 = get_default_item(1), get_default_item(2),get_default_item(3)
    catalog.add(item3)
    catalog.add(item2)
    catalog.add(item1)
    i = 3
    for item in catalog:
        assert item.id == str(i)
        i-=1
