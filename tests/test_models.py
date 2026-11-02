import pytest

from catalog.errors import WrongEntity
from catalog.models import Category, MediaItem


def test_media_item_valid():
    """Test normal media item creation"""
    item = MediaItem(
        id="1",
        name="Since I've Been Loving You",
        category=Category.MUSIC,
        year=1970,
        size=17825792,
        author="Led Zeppelin"
    )
    assert item.id == "1"

def test_media_item_invalid():
    """Test wrong media item creation"""
    with pytest.raises(WrongEntity):
        MediaItem(
            id="cyberpunk",
            name="Chippin' in",
            category=Category.MUSIC,
            year=-2077,
            size=8560000,
            author="SAMURAI"
        )
