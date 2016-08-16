# PHP Completions Kit

[![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat)](https://twitter.com/gerardroche)
[![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat)](https://github.com/gerardroche/sublime-phpck)
[![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat)](https://raw.githubusercontent.com/gerardroche/sublime-phpck/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-phpck.svg?style=flat)](https://github.com/gerardroche/sublime-phpck/stargazers)

[![Sublime version](https://img.shields.io/badge/sublime-v2|v3-lightgrey.svg?style=flat)](https://sublimetext.com)
[![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-phpck.svg?label=release&style=flat&maxAge=2592000)](https://github.com/gerardroche/sublime-phpck/tags)
[![Downloads](https://img.shields.io/packagecontrol/dt/PHP%20Completions%20Kit.svg?style=flat&maxAge=2592000)](https://packagecontrol.io/packages/PHP%20Completions%20Kit)

PHP completions for Sublime Text.

## Works best with [PHP Grammar], [PHP Snippets], and [PHPUnit].

## Overview

* [Features](#features)
* [Key Bindings](#key-bindings)
* [Installation](#installation)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

# Features

* PHP [~7.0](http://semver.org)
* [PSR](http://www.php-fig.org) compliant
* Scoped to minimise auto-complete noise
* Language constructs
* Magic constants
* Magic methods
* Constants
* Functions
* Type hints e.g. begin typing at `class Name extends |`, `function(|`, `/* @var | */`, and any other scope where a type hint is valid.
    + Exception type hints only e.g. begin typing at `try { } catch(|`
    + Interface type hints only e.g. begin typing at `class name implements |`
    + Instantiable classes only e.g. begin typing at `new |`
* Supported extensions:
    ```
    bcmath  bz2 calendar Core ctype  curl  date  dom ereg exif fileinfo filter
    ftp  gd  gettext hash iconv  intl  json  libxml  mbstring  mcrypt  mhash
    mysql  mysqli  mysqlnd openssl  pcntl pcre PDO  pdo_mysql pdo_sqlite Phar
    posix  readline  Reflection  session shmop  SimpleXML soap sockets  SPL
    sqlite3  standard  sysvmsg sysvsem  sysvshm tidy tokenizer  wddx  xdebug
    xml xmlreader  xmlwriter Zend OPcache zip  zlib
    ```

## Key Bindings

| OS X | Windows | Linux | Description |
|------|---------|-------|-------------|
| <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Alt</kbd>+<kbd>/</kbd> | Activate completions |

To enable [tab-completions](http://docs.sublimetext.info/en/latest/extensibility/completions.html#tab-completed-completions) set `"tab_completion": true` in `Preferences > Settings - User`.

## Installation

To use the old PHP 5.6 completions, manually install via Git and checkout the 5.x branch.

### Package Control installation

The preferred method of installation is via [Package Control].

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named `php-completions` in the Sublime Text Packages directory for your platform:
    * Sublime Text 3
        - Linux: `git clone https://github.com/gerardroche/sublime-phpck.git ~/.config/sublime-text-3/Packages/php-completions`
        - OS X: `git clone https://github.com/gerardroche/sublime-phpck.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/php-completions`
        - Windows: `git clone https://github.com/gerardroche/sublime-phpck.git %APPDATA%\Sublime/ Text/ 3/Packages/php-completions`
    * Sublime Text 2
        - Linux: `git clone https://github.com/gerardroche/sublime-phpck.git ~/.config/sublime-text-2/Packages/php-completions`
        - OS X: `git clone https://github.com/gerardroche/sublime-phpck.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/php-completions`
        - Windows: `git clone https://github.com/gerardroche/sublime-phpck.git %APPDATA%\Sublime/ Text/ 2/Packages/php-completions`
3. The features listed above will be available the next time Sublime Text is started.

## Contributing

Your issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).

[Package Control]: https://packagecontrol.io/browse/authors/gerardroche
[PHP Grammar]: https://packagecontrol.io/browse/authors/gerardroche
[PHP Completions]: https://packagecontrol.io/browse/authors/gerardroche
[PHP Snippets]: https://packagecontrol.io/browse/authors/gerardroche
[PHPUnit]: https://packagecontrol.io/browse/authors/gerardroche
[PHPUnit Completions]: https://packagecontrol.io/browse/authors/gerardroche
[PHPUnit Snippets]: https://packagecontrol.io/browse/authors/gerardroche
