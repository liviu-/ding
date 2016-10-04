# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project pretends to adhere to [Semantic Versioning](http://semver.org/).

## [1.3.0] - 2016-10-04

### Changed

- Eliminated effect on scrollback buffer: all the printed countdown steps were preserved in the terminal creating a long scrollback especially for big waiting times ([andars](https://github.com/andars) #4)
- Changed the regex in the help message for the 3rd time. The previous regex was wrong as it was indicating that 1h3m is valid input while the tool expects them to be separated by space.

## [1.2.0] - 2016-10-03

### Added
- Added Windows support

### Changed
- Updated regex from the help section to make it smaller and easier to understand hopefully. 

## [1.1.0]  - 2016-10-02

### Added
- Added a countdown for the script

### Changed
- Updated regex from the help section.

## [1.0.0] - 2016-10-02

### Added
- Added more tests including integration tests, tox, travis for py26, py27, py32, py33, py34, py35, and python nightly
- Added usage gif to the README.md file
- Added this change log

## [0.0.1] - 2016-10-02

Initial stable release

[1.3.0]: https://github.com/liviu-/ding/compare/v1.2.0..v1.3.0
[1.2.0]: https://github.com/liviu-/ding/compare/v1.1.0..v1.2.0
[1.1.0]: https://github.com/liviu-/ding/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/liviu-/ding/compare/v0.0.1...v1.0.0
[0.0.1]: https://github.com/liviu-/ding/tree/v0.0.1
