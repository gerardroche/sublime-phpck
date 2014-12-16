CHANGELOG
=========

0.5.2
-----

- Fixed Functions and language constructs should not trigger in a comment context fd0346e43e12cc4ed85b81366ff123d9914b72e6
- Added Simplified magic method __construct and __invoke argument fields c29906a4c633f648faadbb981a9de445ed4df9b8

0.5.1
-----

- Fixed Completions should not trigger in a string context Merge pull request #6 from MattDMo/master

0.5.0
-----

- Updated completions to PHP version 5.6.0 ee77ec49c5deeaf22311e175154bf07fc4b4b476


0.4.0
-----

- Updated completions to PHP version 5.5.13 1619f288cc8b949d69541e72be542d25ca72de4c

0.3.8
-----

- Fixed `use |` was not triggering type hints fc1791efe7b5d820f5f039e7eb779714e22ab9be 76666a046871bbdbd5e0cf34b300a8c50712b324

0.3.7
-----

- Fixed Functions should not trigger in a ckass instantiation context f3c334e7508ca4ca02c885666afe938a61963890

0.3.6
-----

- Fixed Forgot to bump version in versioning file, again.

0.3.5
-----

- Fixed Should not trigger type hints, functions, or language constructs in a variable context 1374388fec8b7195c765ccdd9739dd2fd64bf9cb

0.3.4
-----

- Fixed Forgot to bump version in versioning file

0.3.3
-----

- Fixed functions and language constructs should not be triggered in PHPDoc or inheritance contexts bd0bc3ce97f1084c1a4c669e14d77d5788f3aba6 699fd2c010775bbb27fc6409ec1f0d3646b6e1d8 e5dd12da7af4f5000136df95df05c59a925d0388
- Fixed Exception type hints were not triggering in an inheritance context bac45cccf2e75b3b13c54c17b300f5a6b19365d7
- Fixed Exception type hints were not trigging in a PHPDoc context b4d0365cebde8f4bf68d88c3801a894912126829
- Fixed Interfaces were not triggering in function argument type hint context 2ca2696bf1af728c66ac4bf1d52fb376efec5707
- Fixed Class, interface, and exception completions were missing descriptions 3c0c8cb6494fc5da39d127c81234088dee87ac16
- Fixed Magic method completions were missing descriptions 10e945161feee467f1cd6b4269fc865fa3d4bb37
- Added Extension name to descriptions fbe93f1c722402a439e9f2fc2372383fe2721451

0.3.2
-----

- Fixed Magic method completions were not working in some contexts 6c299d1238ea64119039846ad8078b51ff90aac9
- Fixed Keyword completions were not working in some contexts c6ef3d255bbf9a31a3ff844a9d8ac546017d5417
- Fixed Compile-time constant missing descriptions 3d9b8fcf980ce61ea068c1161bd2c2a4f12db429

0.3.1
-----

- Fixed #2 missing some language construct functions e.g. isset 6b93329b04492193a68620bc88aafbfd06301f7e
- Fixed Language construct functions now have labels/descriptions 68602acdbdf3129080033c5c3a22d0d143fb7120

0.3.0
-----

- Fixed Missing license: Added BSD (3-Clause) http://choosealicense.com/licenses/#bsd-3 59ec13923e3a6ee9cb7ba10abba8bbe525778b08
- Updated completions to PHP version 5.5.11 b0fa88aa84ea4281ff0a69874836686e99f1ebc7

0.2.0
-----

- Fixed Type hint completions should trigger in PHPDoc context eeb454e87e89f1bd19395df88ef49a8ebfa955ed
- Added CURL extension completions 71d848a12798fc5439172b7a2478262e12da43e4
- Added Tidy extension completions e2abbee49d261380b2485416550ec5964e99bbae
- Added SQLite version 3 databases extension completions 4cddf83b5185151cbf9cccc5af1fc63120371089

0.1.1
-----

- Fixed Type hint completions should trigger in function argument context c1d9d19e8ef1c146ff02b452c8d2370325ec4bc8
- Fixed Deprecated function descriptions should be right-aligned de7346e2537183b562f0e720bb476e4f5fca2cc3
- Fixed #1 Error Loading Completions; Only affects Sublime Text 2
- Fixed instantiable class completions should not trigger in exception catch blocks 27b885fa9d729f8ee9c5335ff583eaeaf257dc3f

0.1.0
-----

- Initial import: PHP 5.4 completions
