# Changelog


## [Unreleased]


### Changed

- PySheds has migrated from `mdbartos/pysheds` to `pysheds/pysheds` and is now being managed by a collective of maintainers.
- `pysheds` now records changes, deprecations, and other pertinant information using the [Keep A Changelog](https://keepachangelog.com/en/1.1.0/) approach.
- Pull Requestss for `pysheds` are now tested across all supported Python versions on GitHub Workflows CI. 

### Removed

- Python versions below 3.10 are no longer supported. Support has beeen extended for Python versions from 3.11 to 3.14.

### Security

- GitHub Actions and Python dependencies found running in CI workflows are now pinned to commit hashes, rather than mutable tags.

## 0.5

### Fixed

- Ensure compatibility with numpy 2+.

### Removed

- Remove pgrid and rfsm.

## 0.4

### Added

- Add type checking of nodata values. (#228)
- Add Python3.12 support. (#242)
- Add priority flood algorithm for depression filling. (#243)

### Fixed

- Fix bugs in D8 routing for border cells and nodata cells. (#235)
- Correctly initialize output and handle nodata cases. (#236)
- Fix deprecated np.bool_ type. (#245)

## 0.3.5

### Changed

- Updated GitHub Actions to their newest version and package-building workflow to support Python3.11.builds
- Enable keyword arguments of to_raster to propagate to rasterio.

### Added

- Added support for Python3.11.
- Added package classifiers to better describe pysheds on PyPI, including support on Python3.11.
- Added installer recipes (pysheds[dev] and pysheds[recipes]), to install the necessary packages for running tests and notebooks, respectively.
- Added long description to setup.py.


### Removed

- Removed deprecated pyproj conventions.
- Removed several bare exceptions. Now using ModuleNotFound and ImportError where appropriate.

## 0.3.3

### Added

- Implement extract_profiles function in numba.

### Fixed

- Fix issue with read_band in multiband rasters.

## 0.3.2

### Changed

- Make spatial referencing functions compatible with 3D rasters.
- Rewrite View functions to reduce copying.

### Added

- Add multiple flow direction (MFD) routing.
- Add heap queue to make distance_to_outlet computation more efficient.
- Create MultiRaster class to handle 3D MFD Rasters.

## 0.3.1

### Changed

- Use iterative functions over recursive functions by default.
- Have view inherit nodata value from input raster by default.

### Added

- Add iterative versions of all recursive hydrologic functions.

### Fixed 

- Ensure consistency of viewfinder shape and mask.

## 0.3

### Changed

- Refactor spatial referencing API.

### Added

- Add numba acceleration.

## 0.2.7.1

Initial release target for zenodo.


## 0.2.7

### Fixed

- Fix pyproj dependency.
