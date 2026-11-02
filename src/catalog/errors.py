class CatalogError(Exception):
    """Base error for Catalog"""

class WrongEntity(CatalogError):
    """Raised when MediaItem has wrong fields"""

class IDDuplicate(CatalogError):
    """Raised when MediaItem has duplicate IDs"""

class MediaItemNotFound(CatalogError):
    """Raised when MediaItem is not found"""

class UnsupportedFormatVersion(CatalogError):
    """Raised when MediaItem has unsupported format"""

class DamagedFile(CatalogError):
    """Raised when MediaItem is damaged"""
