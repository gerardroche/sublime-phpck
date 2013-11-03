Sublime PHP Completions Kit
===========================

Provides completions for PHP 5.4.

Removing the Sublime Text default PHP completions
-------------------------------------------------

> **Overriding Files From a Zipped Package**
>
> To override a file in an existing package, just create a file with the same
> name under the `Packages/<Package Name>` directory.
>
> For example to override the file `function.sublime-snippet` in the
> `Python.sublime-package` package that ships with Sublime Text, create a
> directory called `Python` under the `<data_path>/Packages` directory, and
> place your `function.sublime-snippet` file there.
>
> - http://www.sublimetext.com/docs/3/packages.html

1. Locate your Sublime Text `Packages` directory by using the menu item
   `Preferences -> Browse Packages...`
2. Create a directory named `PHP`
3. Create a file named `PHP.sublime-completions` in the `PHP` directory
4. Done!

The blank file you create, `PHP/PHP.sublime-completions`, overrides the default
`PHP/PHP.sublime-completions`. *Doing this stops them from being loaded.*
