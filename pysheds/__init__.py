from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pysheds")
except PackageNotFoundError:
    __version__ = "999"

__all__ = [
    # All other imports go here ...
    "__version__",
]