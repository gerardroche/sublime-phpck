# gerardroche/sublime-php-completions

[![Author](http://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat)](https://twitter.com/gerardroche)
[![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat)](https://github.com/gerardroche/sublime-phpck)
[![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-phpck.svg?style=flat)](https://github.com/gerardroche/sublime-phpck/stargazers)
[![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat)](https://raw.githubusercontent.com/gerardroche/sublime-phpck/master/LICENSE)

[![Sublime version](https://img.shields.io/badge/sublime-v2|v3-lightgrey.svg?style=flat)](http://sublimetext.com)
[![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-phpck.svg?maxAge=2592000?style=flat&label=release)](https://github.com/gerardroche/sublime-phpck/tags)
[![Downloads](https://img.shields.io/packagecontrol/dt/PHP%20Completions%20Kit.svg?maxAge=2592000?style=flat)](https://packagecontrol.io/packages/PHP%20Completions%20Kit)

PHP completions for Sublime Text.

Works best with [PHP Grammar], [PHP Snippets], and [PHPUnit].

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

The preferred method of installation is via Package Control.

1. Install [Package Control](https://packagecontrol.io).
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows, Linux) or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `PHP Completions Kit` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text to complete installation. The features listed above should now be available.

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

[PHP Grammar]: https://packagecontrol.io/packages/php-grammar
[PHP Completions]: https://packagecontrol.io/packages/PHP%20Completions%20Kit
[PHP Snippets]: https://packagecontrol.io/packages/php-snippets
[PHPUnit]: https://github.com/gerardroche/sublime-phpunit
[PHPUnit Completions]: https://github.com/gerardroche/sublime-phpunit-completions
[PHPUnit Snippets]: https://github.com/gerardroche/sublime-phpunit-snippets
