# PHP Completions Kit

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Version](https://img.shields.io/github/tag/gerardroche/sublime-phpck.svg?style=flat-square&label=version)](https://github.com/gerardroche/sublime-phpck/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-phpck.svg?style=flat-square)](https://github.com/gerardroche/sublime-phpck/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/PHP%20Completions%20Kit.svg?style=flat-square)](https://packagecontrol.io/packages/PHP%20Completions%20Kit)

Provides PHP completions for Sublime Text.

# FEATURES

* PHP ~7
* Scoped to minimise auto-complete noise
* Language constructs
* Magic constants
* Magic methods
* Constants
* Functions
* Type hints: Classes, Interfaces, Exceptions, Instantiables, etc.
* Supported extensions: `bcmath`, `bz2`, `calendar`, `Core`, `ctype`, `curl`, `date`, `dom`, `ereg`, `exif`, `fileinfo`, `filter`, `ftp`, `gd`, `gettext`, `hash`, `iconv`, `intl`, `json`, `libxml`, `mbstring`, `mhash`, `mysql`, `mysqli`, `mysqlnd`, `openssl`, `pcntl`, `pcre`, `PDO`, `pdo_mysql`, `pdo_sqlite`, `Phar`, `posix`, `readline`, `Reflection`, `session`, `shmop`, `SimpleXML`, `soap`, `sockets`, `SPL`, `sqlite3`, `standard`, `sysvmsg`, `sysvsem`, `sysvshm`, `tidy`, `tokenizer`, `wddx`, `xdebug`, `xml`, `xmlreader`, `xmlrpc`, `xmlwriter`, `xsl`, `Zend`, `OPcache`, `zip`, `zlib`.
* PSR compatible

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named `PHP Completions Kit` in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-phpck.git ~/.config/sublime-text-3/Packages/PHP Completions Kit`
* OSX: `git clone https://github.com/gerardroche/sublime-phpck.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/PHP Completions Kit`
* Windows: `git clone https://github.com/gerardroche/sublime-phpck.git %APPDATA%\Sublime/ Text/ 3/Packages/PHP Completions Kit`

## USAGE

By default, completions are triggered automatically when typing. If the setting `auto_complete` is set to false then completions must be manually triggered.

Completions are context aware, meaning they are only provided in relevant contexts e.g. type hints will trigger at `class Name extends |`, `function(|`, `/* @var | */`, exception trigger at `try {} catch(|`, interfaces at `class name implements |`, instantiables `new |`, etc.

Relating Sublime Text key bindings:

OS X | Windows | Linux | Description
-----|---------|-------|------------
<kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | <kbd>Alt</kbd>+<kbd>/</kbd> | Activate completions

Relating Sublime Text settings:

```text
{
    // By default, auto complete will commit the current completion on enter.
    // This setting can be used to make it complete on tab instead.
    // Completing on tab is generally a superior option, as it removes
    // ambiguity between committing the completion and inserting a newline.
    "auto_complete_commit_on_tab": false,

    // Controls if auto complete is shown when snippet fields are active.
    // Only relevant if auto_complete_commit_on_tab is true.
    "auto_complete_with_fields": false,
}
```

Set them globally: **Menu → Preferences → Settings**:

```json
{
    "auto_complete_commit_on_tab": true,
    "auto_complete_with_fields": true
}
```

Set them per-project: **Menu → Project → Edit Project**:

```json
{
    "settings": {
        "auto_complete_commit_on_tab": true,
        "auto_complete_with_fields": true
    }
}
```

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
