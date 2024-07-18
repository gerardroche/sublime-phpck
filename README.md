# PHP Completions Kit

<div>
    <p>
        <a href="https://packagecontrol.io/packages/PHP Completions Kit">
            <img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/PHP Completions Kit?style=for-the-badge">
        </a>
        <a href="https://github.com/gerardroche/sublime-phpck/stargazers">
            <img alt="Stars" src="https://img.shields.io/github/stars/gerardroche/sublime-phpck?style=for-the-badge&logo=starship">
        </a>
        <a href="https://x.com/intent/follow?screen_name=gerardroche_">
            <img alt="Follow on X" src="https://img.shields.io/twitter/follow/gerardroche_?style=for-the-badge&logo=x">
        </a>
    </p>
</div>

PHP completions for Sublime Text.

## ✨ Features

- 🔥 PHP `>= 8.2`
- ⚡ Scoped to minimise auto-complete noise.
- 🚀 Language constructs, methods, constants, functions, type hints including classes, interfaces, and exceptions.
- 📦 Supported extensions: `bcmath`, `bz2`, `calendar`, `Core`, `ctype`, `curl`, `date`, `dom`, `ereg`, `exif`, `fileinfo`, `filter`, `ftp`, `gd`, `gettext`, `hash`, `iconv`, `intl`, `json`, `libxml`, `mbstring`, `mhash`, `mysql`, `mysqli`, `mysqlnd`, `openssl`, `pcntl`, `pcre`, `PDO`, `pdo_mysql`, `pdo_sqlite`, `Phar`, `posix`, `readline`, `Reflection`, `session`, `shmop`, `SimpleXML`, `soap`, `sockets`, `SPL`, `sqlite3`, `standard`, `sysvmsg`, `sysvsem`, `sysvshm`, `tidy`, `tokenizer`, `wddx`, `xdebug`, `xml`, `xmlreader`, `xmlrpc`, `xmlwriter`, `xsl`, `Zend`, `OPcache`, `zip`, `zlib`

## Installation

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named `PHP Completions Kit` in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-phpck.git ~/.config/sublime-text-3/Packages/PHP Completions Kit`
* OSX: `git clone https://github.com/gerardroche/sublime-phpck.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/PHP Completions Kit`
* Windows: `git clone https://github.com/gerardroche/sublime-phpck.git %APPDATA%\Sublime/ Text/ 3/Packages/PHP Completions Kit`

## Usage

OS X | Windows | Linux | Description
-----|---------|-------|------------
`Ctrl+Space` | `Ctrl+Space` | `Alt+/` | Activate completions

## Settings

Setting | Default | Description
------- | ------- | -----------
`auto_complete` | `true` | Enable auto complete to be triggered automatically when typing.
`auto_complete_commit_on_tab` | `false` | By default, auto complete will commit the current completion on enter. This setting can be used to make it complete on tab instead. Completing on tab is generally a superior option, as it removes ambiguity between committing the completion and inserting a newline.
`auto_complete_with_fields` | `false` | Controls if auto complete is shown when snippet fields are active. Only relevant if auto_complete_commit_on_tab is true.

**Menu → Preferences → Settings**:

```json
{
    "auto_complete_commit_on_tab": true,
    "auto_complete_with_fields": true
}
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
