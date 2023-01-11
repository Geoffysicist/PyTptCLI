"""Module1 - A one line summary of the module or program, terminated by a period.
Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
  Typical usage example:
  foo = SampleClass()
  
  bar = foo.public_method(required_variable, optional_variable=42)
"""

import argparse
from pathlib import Path
import yaml
import sys

class SampleClass(object):
    """Summary of class here.
    Longer class information after leaving a line...
    
    Attributes:
        likes_spam (type): indicates if we like SPAM or not.
        eggs (type): count of the eggs we have eaten.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self._likes_spam = likes_spam
        self._eggs = 0

    def public_method(self):
        """Short description.
        
        Longer description of desired functionality
        Args:
            required_variable (type): A required argument
            optional_variable (type): An optional argument
        Returns:
            type: nothing but if it did you would describe it here
        Raises:
            NoError: but if it did you would describe it here
        """
        return None

def function_name(required_variable, optional_variable=None):
    """Short description.
    Longer description of desired functionality
    Args:
        required_variable (type): A required argument
        optional_variable (type): An optional argument
    Returns:
        type: nothing but if it did you would describe it here
    Raises:
        NoError: but if it did you would describe it here
    """
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('settings_path', help='the relative path (including filename) to the settings yaml')
    args = parser.parse_args()
    
    settings_pth = Path(args.settings_path)
    
    try:
        with open(settings_pth) as f:
            settings = yaml.safe_load(f)
    except FileNotFoundError as e:
        msg = f'the settings yaml file "{settings_pth}" can not be found'
        print(msg)
        sys.exit('\nExiting\n')
    
    print(settings)
            