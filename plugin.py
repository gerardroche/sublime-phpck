import os

from sublime import packages_path


def plugin_loaded():
    # Disable default PHP package completions
    completions_file = os.path.join(packages_path(), 'PHP', 'PHP.sublime-completions')
    if not os.path.isfile(completions_file):
        try:
            if not os.path.isdir(os.path.dirname(completions_file)):
                os.makedirs(os.path.dirname(completions_file))
            with open(completions_file, 'w+', encoding='utf8') as f:
                f.write('')
        except Exception as e:
            print('PHP Completions Kit: an error occured disabling native snippets ' + str(e))
