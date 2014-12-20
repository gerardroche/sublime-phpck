# PHP Completions Changelog

## 0.6.0

### Bug Fixes

* #8 Show messages when installing and updating
* Some completions like functions and language constructs shouldn't be activated in a class constant scope e.g. `self::|`

## 0.5.2

### Bug Fixes

* Fixed Functions and language constructs should not trigger in a comment context fd0346e
* Added Simplified magic method __construct and __invoke argument fields c29906a

## 0.5.1

### Bug Fixes

* Fixed Completions should not trigger in a string context Merge pull request #6 from MattDMo/master

## 0.5.0

### Bug Fixes

* Updated completions to PHP version 5.6.0 ee77ec4

## 0.4.0

### Bug Fixes

* Updated completions to PHP version 5.5.13 1619f28

## 0.3.8

### Bug Fixes

* Fixed `use |` was not triggering type hints fc1791e 76666a0

## 0.3.7

### Bug Fixes

* Fixed Functions should not trigger in a ckass instantiation context f3c334e

## 0.3.6

### Bug Fixes

* Fixed Forgot to bump version in versioning file, again

## 0.3.5

### Bug Fixes

* Fixed Should not trigger type hints, functions, or language constructs in a variable context 1374388

## 0.3.4

### Bug Fixes

* Fixed Forgot to bump version in versioning file

## 0.3.3

### Bug Fixes

* Fixed functions and language constructs should not be triggered in PHPDoc or inheritance contexts bd0bc3c 699fd2c e5dd12d
* Fixed Exception type hints were not triggering in an inheritance context bac45cc
* Fixed Exception type hints were not trigging in a PHPDoc context b4d0365
* Fixed Interfaces were not triggering in function argument type hint context 2ca2696
* Fixed Class, interface, and exception completions were missing descriptions 3c0c8cb
* Fixed Magic method completions were missing descriptions 10e9451
* Added Extension name to descriptions fbe93f1

## 0.3.2

### Bug Fixes

* Fixed Magic method completions were not working in some contexts 6c299d1
* Fixed Keyword completions were not working in some contexts c6ef3d2
* Fixed Compile-time constant missing descriptions 3d9b8fc

## 0.3.1

### Bug Fixes

* Fixed #2 missing some language construct functions e.g. isset 6b93329
* Fixed Language construct functions now have labels/descriptions 68602ac

## 0.3.0

### Bug Fixes

* Fixed Missing license: Added BSD (3-Clause) http://choosealicense.com/licenses/#bsd-3 59ec139
* Updated completions to PHP version 5.5.11 b0fa88a

## 0.2.0

### Bug Fixes

* Fixed Type hint completions should trigger in PHPDoc context eeb454e

### New Features

* Added CURL extension completions 71d848a
* Added Tidy extension completions e2abbee
* Added SQLite version 3 databases extension completions 4cddf83

## 0.1.1

### Bug Fixes

* Fixed Type hint completions should trigger in function argument context c1d9d19
* Fixed Deprecated function descriptions should be right-aligned de7346e
* Fixed #1 Error Loading Completions; Only affects Sublime Text 2
* Fixed instantiable class completions should not trigger in exception catch blocks 27b885f

## 0.1.0

* Initial import: PHP 5.4 completions
