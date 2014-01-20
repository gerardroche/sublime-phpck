Sublime PHP Completions Kit
===========================

Provides completions for PHP 5.4, includes:

* classes
* interfaces
* exceptions
* functions
* constants
* magic constants
* magic methods

Removing Sublime Text Default PHP Completions
---------------------------------------------

The PHP Completions Kit contains some similar completions that are provided by
the Sublime Text default PHP package. You may want to remove these completions,
you can do this by overriding them:

1. Locate your Sublime Text `Packages` directory by using the menu item
  `Preferences -> Browse Packages...`
2. Create a directory named `PHP`
3. Create a file named `PHP.sublime-completions` inside the `PHP` directory

Done!

For more information see [Overriding Files from a Zip Package].

[Overriding Files from a Zip Package]: http://www.sublimetext.com/docs/3/packages.html

Usage & Features
----------------

These completions try to be as context specific as is possible and trigger
*only* when relevant.

`$...` in function prototypes means and so on. This variable name is used when
a function can take an endless number of arguments.

Instantiables

    new Date|                               <-- triggers intiantiable classes and exceptions
        DateTime()
        DateInterval()
        ...

Inheritance / Type Hints

    class name extends Date|                <-- triggers classes and exceptions

    class name implements Count|            <-- triggers interfaces

    interface name extends Count|           <-- triggers interfaces

    function name(Date|                     <-- triggers classes, interfaces, and exceptions

    class name
    {
        public function name(Date|          <-- triggers classes, interfaces, and exceptions

    ... instanceof Date|                    <-- triggers classes, interfaces, and exceptions

    try {
      // ...
    } catch (Out|                           <-- triggers exeptions
             OutOfRangeException
             OutOfBoundsException
             ...

    /**
     * @param Date|                         <-- triggers classes, interfaces, and exceptions
     * @return Date|                        <-- triggers classes, interfaces, and exceptions
     */

Installation
------------

The recommended way to install and keep up to date is to install it via
[Package Control]. Once you have installed Package Control, open it via
`Preferences -> Package Control` and click on
`Package Control: Install Package`. Type `PHP Completions Kit` into the search
box, then hit enter or click on the result to install.

[Package Control]: https://sublime.wbond.net/installation

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

1. Download the files using the GitHub .zip download option
2. Unzip the files and rename the folder to `sublime-phpck`
3. Find your `Packages` directory using the menu item
  `Preferences -> Browse Packages...`
4. Copy the folder into your Sublime Text `Packages` directory
