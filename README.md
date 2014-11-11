Sublime PHP Completions Kit
===========================

Provides PHP [~5.6](http://semver.org) completions for [Sublime Text](http://www.sublimetext.com).

Completions include [language constructs], [compile-time constants],
constants, functions, classes, interfaces, exceptions, and magic-methods.

[language constructs]: http://php.net/manual/reserved.keywords.php
[compile-time constants]: http://php.net/manual/reserved.keywords.php

Extensions include:

    bcmath  bz2 calendar Core ctype  curl  date  dom ereg exif fileinfo filter
    ftp  gd  gettext hash iconv  intl  json  libxml  mbstring  mcrypt  mhash
    mysql  mysqli  mysqlnd openssl  pcntl pcre PDO  pdo_mysql pdo_sqlite Phar
    posix  readline  Reflection  session shmop  SimpleXML soap sockets  SPL
    sqlite3  standard  sysvmsg sysvsem  sysvshm tidy tokenizer  wddx  xdebug
    xml xmlreader  xmlwriter Zend OPcache zip  zlib

All completions activate *only* in valid contexts.

Other PHP packages:

* [PHP Grammar](https://github.com/gerardroche/sublime-php-grammar)
* [PHP Snippets](https://github.com/gerardroche/sublime-php-snippets)
* [PHPUnit Completions](https://github.com/gerardroche/sublime-phpunitck)

Usage
-----

> Auto complete shows the completion popup as you type, so you can fill in long
> words by typing only a few characters.
>
> Pressing <kbd>ctrl</kbd>+<kbd>space</kbd> (OSX and Windows),
> <kbd>alt</kbd>+<kbd>/</kbd> (Linux) will show the completion popup if it's not
> currently showing.  If it is showing, it'll select the next item.
>
> &mdash; [Sublime Text Documentation](http://www.sublimetext.com/docs/3/auto_complete.html)

**Type hints**

`class name extends |` activates classes and exceptions

`class name implements |` activates interfaces

`interface name extends |` activates interfaces

`... instanceof |` activates classes, interfaces, and exceptions

`function name(|` activates classes, interfaces, and exceptions

`class name { public function name(|` activates classes, interfaces, and exceptions

`try { /*...*/ } catch (|` activates exceptions

    /**
     * @annotation | < activates classes, interfaces, and exceptions
     */

**Instantiable classes**

`new |` activates instantiable classes and exceptions

### Function arguments

Cycle through argument fields by pressing the <kbd>tab</kbd> key.

To break out of a field cycle <kbd>esc</kbd>.  *You can also press
<kbd>tab</kbd> continuously through to the end of the field cycle.*

Optional fields are *group selected* meaning you can skip remaining fields by
deleting them, and breaking out of the field cycle.

**Example**

The [`array_keys`][phpdocs_array_keys] function has two optional arguments:
`search_value` and `strict`.

    array_keys(arg, search_value, strict)

The [`array_keys`][phpdocs_array_keys] function has two optional arguments:
`search_value` and `strict` - `array_keys(arg, search_value, strict)`.

When you first commit the completion you will get:

         current selection
               vvv
    array_keys(arg, search_value, strict)

After you fill in `arg` press <kbd>tab</kbd> and you get:

                           vvvvvvvvvvvvvvvvvvvvvv
    array_keys(array(1,2,3), search_value, strict)

Notice the comma is under current selection.  This is because the last two
arguments are optional.  This gives you a chance to skip the remaining fields by
pressing <kbd>del</kbd> then <kbd>esc</kbd>.  However, if you want the next
optional field then press <kbd>tab</kbd> again and you get:

                             vvvvvvvvvvvv
    array_keys(array(1,2,3), search_value, strict)

Now fill in the `search_value` and press <kbd>tab</kbd>:

                              vvvvvvvv
    array_keys(array(1,2,3), 2, strict)

If you don't want *this* optional field, press <kbd>del</kbd> then
<kbd>esc</kbd>.  However, if you *do* want it, press <kbd>tab</kbd>:

                                vvvvvv
    array_keys(array(1,2,3), 2, strict)

[phpdocs_array_keys]: http://php.net/array_keys

How to disable the default PHP completions
------------------------------------------

The default PHP completions bundled with Sublime Text may cause redundant,
useless duplicate completions in auto complete.

One way to disable these bundled completions is to [override them](http://www.sublimetext.com/docs/3/packages.html).

1. Locate the Sublime Text `Packages` directory by using the menu item
`Preferences -> Browse Packages...`
2. Create a directory named `PHP`
3. Create an empty file named `PHP.sublime-completions` inside the `PHP`
directory

Installation
------------

### [Package Control](https://sublime.wbond.net/installation)

1. Open Package Control: `Preferences -> Package Control`
2. Select `Package Control: Install Package`
3. Type `PHP Completions Kit` into the search box and select the package to
install it

### [Git](http://git-scm.com)

Clone directly into the Sublime Text `Packages` directory.  *Locate the
`Packages` directory by using the menu item
`Preferences -> Browse Packages...`.*

### [Manual](http://www.sublimetext.com/docs/3/packages.html)

1. [Download a release](https://github.com/gerardroche/sublime-phpck/releases)
2. Unzip and copy it to the Sublime Text `Packages` directory.  *Locate the
`Packages` directory by using the menu item
`Preferences -> Browse Packages...`.*
