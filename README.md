Sublime PHP Completions Kit
===========================

Provides completions for PHP 5.4.

Removing Sublime Text default PHP completions
---------------------------------------------

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

Installation
------------

The recommended way to install and keep up to date is to install it via
[Package Control](https://sublime.wbond.net/installation). Once you have
installed Package Control, open it via `Preferences -> Package Control` and
click on `Package Control: Install Package`. Type `PHP Completions Kit` into
the search box, then hit enter or click on the result to install.

### Using Git

Alternatively, if you are a git user, you can install the completions and keep
up to date by cloning the repository directly into your `Packages` directory
in the Sublime Text application settings area.

You can locate your Sublime Text `Packages` directory by using the menu item
`Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the repository using the command
below:

    git clone https://github.com/gerardroche/sublime-phpck.git

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `sublime-phpck`
* Find your `Packages` directory using the menu item
  `Preferences -> Browse Packages...`
* Copy the folder into your Sublime Text `Packages` directory
