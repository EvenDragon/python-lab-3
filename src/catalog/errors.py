class CatalogError(Exception):
    """Base error for Catalog"""

class WrongEntity(CatalogError):
    """Raised when MediaItem has wrong fields"""
