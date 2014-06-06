Sublime PHP Completions Kit
===========================

Provides PHP 5.5 completions for [Sublime Text](http://www.sublimetext.com).

> Auto complete shows the completion popup as you type, so you can fill in long
> words by typing only a few characters. &mdash; [Sublime Text Documentation](http://www.sublimetext.com/docs/3/auto_complete.html)

Completions include [language constructs], [compile-time constants],
constants, functions, classes, interfaces, exceptions, and magic-methods.

[language constructs]: http://php.net/manual/reserved.keywords.php
[compile-time constants]: http://php.net/manual/reserved.keywords.php

All completions activate *only* in valid contexts.

Other completion kits:

* [Sublime PHPUnit Completions Kit](https://github.com/gerardroche/sublime-phpunitck)

Usage
-----

> Pressing <kbd>ctrl</kbd>+<kbd>space</kbd> (OSX and Windows),
> <kbd>alt</kbd>+<kbd>/</kbd> (Linux) will show the completion popup if it's not
> currently showing.  If it is showing, it'll select the next item.
> &mdash; [Sublime Text Documentation](http://www.sublimetext.com/docs/3/auto_complete.html)

`*` activates [language constructs], [compile-time constants],
functions, constants, etc.

Type hints

`class name extends *` activates classes and exceptions

`class name implements *` activates interfaces

`interface name extends *` activates interfaces

`... instanceof *` activates classes, interfaces, and exceptions

`function name(*` activates classes, interfaces, and exceptions

`class name { public function name(*` activates classes, interfaces, and exceptions

`try { /* ... */ } catch (*` activates exceptions

    /**
     * @annotation * activates classes, interfaces, and exceptions
     */

Instantiable classes

`new *` activates instantiable classes and exceptions

### Function arguments

You can cycle through argument fields by pressing the <kbd>tab</kbd> key.  To
break out of a field cycle at any time press <kbd>esc</kbd>.

**Optional fields** are *group selected* meaning you can skip any remaining
optional fields at any time by deleting them i.e. by pressing <kbd>del</kbd>
, then break out of the field cycle by pressing <kbd>esc</kbd>.

*To break out of a field cycle after deleting fields, you can also press
<kbd>tab</kbd> continuously until the end of the field cycle.*

**Example**

The [`array_keys`][phpdocs_array_keys] function has two optional arguments,
`search_value` and `strict`.

    array_keys(arg, search_value, strict)

When you first commit the completion you will get:

         current selection
               vvv
    array_keys(arg, search_value, strict)

After you fill in `arg` press <kbd>tab</kbd> and you get:

                              current selection
                           vvvvvvvvvvvvvvvvvvvvvv
    array_keys(array(1,2,3), search_value, strict)

Notice the comma is under current selection.  This is because the last two
arguments are optional.  This gives you a chance to skip the remaining fields by
pressing <kbd>del</kbd> then <kbd>esc</kbd>.  However, if you want the next
optional field then press <kbd>tab</kbd> again and you get:

                           current selection
                             vvvvvvvvvvvv
    array_keys(array(1,2,3), search_value, strict)

Now fill in the `search_value` and press <kbd>tab</kbd>:

                           current selection
                              vvvvvvvv
    array_keys(array(1,2,3), 2, strict)

If you don't want *this* optional field, press <kbd>del</kbd> then
<kbd>esc</kbd>.  However, if you *do* want it, press <kbd>tab</kbd>:

                            current selection
                                vvvvvv
    array_keys(array(1,2,3), 2, strict)

[phpdocs_array_keys]: http://php.net/array_keys

How to remove the default PHP completions
-----------------------------------------

You may want to remove the default PHP completions provided by Sublime Text
because they cause duplicate completions.

The only way I know how to fix this is by [overriding the defaults](http://www.sublimetext.com/docs/3/packages.html).

1. Locate your Sublime Text `Packages` directory by using the menu item
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

Clone directly into your Sublime Text `Packages` directory.  *Locate your
`Packages` directory by using the menu item
`Preferences -> Browse Packages...`.*

### [Manual](http://www.sublimetext.com/docs/3/packages.html)

1. [Download a release](https://github.com/gerardroche/sublime-phpck/releases)
2. Unzip and copy it to your Sublime Text `Packages` directory.  *Locate your
`Packages` directory by using the menu item
`Preferences -> Browse Packages...`.*
