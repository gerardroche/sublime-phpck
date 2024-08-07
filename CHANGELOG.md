# PHP Completions Kit Changelog

## 1.15.1 - 2023-08-09

- Upgrade PHP 8.2.9

## 1.15.0 - 2023-04-01

- Added: Update to PHP 8.2

## 1.14.0 - 2022-12-16

- Added: Enriched annotations and details

## 1.13.1 - 2022-09-25

- Fixed: Parse errors when details contains unescaped ampersand character

## 1.13.0 - 2022-09-15

- Added: Argument and return type details in autocomplete popup

## 1.12.0 - 2022-09-12

- Added: Update to PHP 8.1.0
- Fixed: Various fixes

## 1.11.0 - 2020-12-16

- Added: Update to PHP 8.0.9

## 1.10.0 - 2020-11-03

- Added: Update to latest PHP 8.0-dev
- Fixed [#15](https://github.com/gerardroche/sublime-phpck/issues/15): Some completions failed.

## 1.9.0 - 2020-04-29

- Added: Support for ST4 completions

## 1.8.0 - 2020-04-28

- Added: Argument type hints
- Added: Update to PHP 8.0-dev

## 1.7.0 - 2020-01-24

- Added: Update to PHP 7.4.1

## 1.6.0

- Added: Update to support ST4

## 1.5.0

- Added: Update to 7.3.0

## 1.4.0

- Added: Update to 7.2.6

## 1.3.0

- Added: Return type hints
- Fixed [#11](https://github.com/gerardroche/sublime-phpck/issues/11): bool is auto-completed to boolval() in return typ

## 1.2.0 - 2017-12-08

- Added: Updated to 7.2.0

## 1.1.0 - 2017-08-09

- Added: `xmlrpc` and `xsl` extensions

## 1.0.1 - 2017-08-09

- Update to PHP 7.1.8

## 1.0.0 - 2017-05-31

- Version 1.0.0 release :)

## 0.18.0

- Update to PHP 7.1.1

## 0.17.0

- Update to PHP 7.0.9
- Fixed: #10 several issues with scopes in newer builds of ST

## 0.16.0

- Update to PHP 7.0.8

## 0.15.0

- Update to PHP 7.0.5

## 0.14.0

- Update to PHP 5.6.20

## 0.13.0

- Fixed: Work around ST issues when triggers contain certain characters. Completions are broken in a various ways when completion triggers contain characters not in range [a-zA-Z0-9_-]. See https://github.com/SublimeTextIssues/Core/issues/1061, and https://github.com/SublimeTextIssues/Core/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+completions.
- Removed: package control messages; the changelog is good enough

## 0.12.0

- Added: Auto disable native PHP package completions
- Added: Package Settings Menu with README, CHANGELOG, and LICENSE links
- Added: Update to PHP 5.6.14

## 0.11.0

- Added: Update to PHP 5.6.9

## 0.10.0

- Fixed: Forgot to add package control changelog messages

## 0.9.0

- Fixed: `true`, `false`, and `null` core constants should be lowercase in-line with PSR

## 0.8.0

- Added: PHP 5.6 `__debugInfo` magic method
- Changed: "Compile-Time Constant" description changed to "Magic Constant" as per PHP documentation.

## 0.7.0

- Added: Annotations are now available in multi line comments, not just phpdoc's e.g. `/* @annotation `
- Added: Minimise auto-complete noise: Functions and language constructs no longer activate in a "meta" scope e.g. typing at `class a extends |`
- Added: Type hints are now available in multi line comments, not just phpdocs's e.g. begin typing at `/* @var |`
- Changed: Scopes are now sorted ASC
- Changed: Scopes blacklists are now pretty printed

## 0.6.0

- Fixed: #8 Show messages when installing and updating
- Fixed: Some completions like functions and language constructs shouldn't be activated in a class constant scope e.g. `self::|`

## 0.5.2

- Added: Simplified magic method `__construct` and `__invoke` argument fields c29906a

- Fixed: Functions and language constructs should not trigger in a comment context fd0346e

## 0.5.1

- Fixed: Completions should not trigger in a string context Merge pull request #6 from MattDMo/master

## 0.5.0

- Added: Updated to PHP version 5.6.0 ee77ec4

## 0.4.0

- Added: Updated to PHP version 5.5.13 1619f28

## 0.3.8

- Fixed: `use |` was not triggering type hints fc1791e 76666a0

## 0.3.7

- Fixed: Functions should not trigger in a ckass instantiation context f3c334e

## 0.3.6

- Fixed: Forgot to bump version in versioning file, again

## 0.3.5

- Fixed: Should not trigger type hints, functions, or language constructs in a variable context 1374388

## 0.3.4

- Fixed: Forgot to bump version in versioning file

## 0.3.3

- Fixed: functions and language constructs should not be triggered in PHPDoc or inheritance contexts bd0bc3c 699fd2c e5dd12d
- Fixed: Exception type hints were not triggering in an inheritance context bac45cc
- Fixed: Exception type hints were not trigging in a PHPDoc context b4d0365
- Fixed: Interfaces were not triggering in function argument type hint context 2ca2696
- Fixed: Class, interface, and exception completions were missing descriptions 3c0c8cb
- Fixed: Magic method completions were missing descriptions 10e9451
- Fixed: Extension name to descriptions fbe93f1

## 0.3.2

- Fixed: Magic method completions were not working in some contexts 6c299d1
- Fixed: Keyword completions were not working in some contexts c6ef3d2
- Fixed: Compile-time constant missing descriptions 3d9b8fc

## 0.3.1

- Fixed: #2 missing some language construct functions e.g. isset 6b93329
- Fixed: Language construct functions now have labels/descriptions 68602ac

## 0.3.0

- Added: Updated to PHP version 5.5.11 b0fa88a
- Fixed: Missing license: Added BSD (3-Clause) s59ec139

## 0.2.0

- Added: CURL extension completions 71d848a
- Added: SQLite version 3 databases extension completions 4cddf83
- Added: Tidy extension completions e2abbee
- Fixed: Type hint completions should trigger in PHPDoc context eeb454e

## 0.1.1

- Fixed: Type hint completions should trigger in function argument context c1d9d19
- Fixed: Deprecated function descriptions should be right-aligned de7346e
- Fixed: #1 Error Loading Completions; Only affects Sublime Text 2
- Fixed: instantiable class completions should not trigger in exception catch blocks 27b885f

## 0.1.0

- Initial import: PHP 5.4 completions
