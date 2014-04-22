Sublime PHP Completions Kit
===========================

Provides PHP 5.5 completions for [Sublime Text][st].

> [Auto complete shows the completion popup as you type, so you can fill in long
> words by typing only a few characters.](http://www.sublimetext.com/docs/3/auto_complete.html)

[st]: http://www.sublimetext.com

Usage & Features
----------------

Completions include [language constructs], constants, magic constants,
functions, classes, interfaces, exceptions, and magic methods.

[language constructs]: http://php.net/manual/reserved.keywords.php

### Function arguments

You can cycle through argument fields by pressing the <kbd>Tab</kbd> key.  To
break out of a field cycle at any time press <kbd>Esc</kbd>.

**Optional fields** are *group selected* meaning you can skip any remaining
optional fields at any time by deleting them i.e. by pressing <kbd>DEL</kbd>
, then break out of the field cycle by pressing <kbd>ESC</kbd>.

*To break out of a field cycle after deleting fields, you can also press
<kbd>TAB</kbd> continuously until the end of the field cycle.*

**Example**

The [`array_keys`][phpdocs_array_keys] function has two optional arguments,
`search_value` and `strict`.

    array_keys(arg, search_value, strict)

When you first commit the completion you will get:

         current selection
               vvv
    array_keys(arg, search_value, strict)

After you fill in `arg` press <kbd>TAB</kbd> and you get:

                              current selection
                           vvvvvvvvvvvvvvvvvvvvvv
    array_keys(array(1,2,3), search_value, strict)

Notice the comma is under current selection.  This is because the last two
arguments are optional.  This gives you a chance to skip the remaining fields by
pressing <kbd>DEL</kbd> then <kbd>ESC</kbd>.  However, if you want the next
optional field then press <kbd>TAB</kbd> again and you get:

                           current selection
                             vvvvvvvvvvvv
    array_keys(array(1,2,3), search_value, strict)

Now fill in the `search_value` and press <kbd>TAB</kbd>:

                           current selection
                              vvvvvvvv
    array_keys(array(1,2,3), 2, strict)

If you don't want *this* optional field, press <kbd>DEL</kbd> then
<kbd>ESC</kbd>.  However, if you *do* want it, press <kbd>TAB</kbd>:

                            current selection
                                vvvvvv
    array_keys(array(1,2,3), 2, strict)

[phpdocs_array_keys]: http://php.net/array_keys

### Context Specific

The completions are context specific, they should trigger *only* in relevant
contexts.

**Examples**

*The pipe character `|` denotes the cursor position when completions are
triggered.*

Instantiables

    new |                       triggers classes/exceptions

Inheritance

    class name extends |        triggers classes/exceptions
    class name implements |     triggers interfaces
    interface name extends |    triggers interfaces

Type hints

    function name(|             triggers classes/interfaces/exceptions
    ... instanceof |            triggers classes/interfaces/exceptions

    class name
    {
        public function name(|  triggers classes/interfaces/exceptions

    try {
      // ...
    } catch (|                  triggers exeptions

PHPDoc

    /**
     * @param |                 triggers classes/interfaces/exceptions
     * @return |                triggers classes/interfaces/exceptions
     */

### Removing the default PHP completions

You may want to remove the default PHP completions provided by Sublime Text
because they cause duplicate completions.

The only way I know how to fix this is by overriding the defaults.

1. Locate your Sublime Text `Packages` directory by using the menu item
`Preferences -> Browse Packages...`
2. Create a directory named `PHP`
3. Create an empty file named `PHP.sublime-completions` inside the `PHP`
directory

For more information read [overriding files from a zip package].

[overriding files from a zip package]: http://www.sublimetext.com/docs/3/packages.html

Installation
------------

### Using [Package Control]

1. Open Package Control: `Preferences -> Package Control`
2. Select `Package Control: Install Package`
3. Type `PHP Completions Kit` into the search box and select the package to
install it.

[Package Control]: https://sublime.wbond.net/installation

### Using [Git]

Clone directly into your Sublime Text `Packages` directory.

*Locate your `Packages` directory by using the menu item
`Preferences -> Browse Packages...`.*

[Git]: http://git-scm.com

### [Manual]

1. [Download a Sublime PHP Completions Kit release from GitHub]
2. Unzip it and copy it to your Sublime Text `Packages` directory. *Find your
`Packages` directory by clicking the `Preferences -> Browse Packages...` menu*

[Manual]: http://www.sublimetext.com/docs/3/packages.html
[Download a Sublime PHP Completions Kit release from GitHub]: https://github.com/gerardroche/sublime-phpck/releases
