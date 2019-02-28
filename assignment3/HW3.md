# Homework Assignment #3

## Date: 08-04-2018
## Due date: 22-04-2018, 15:00

1. _Duplicates Discovery:_
Define a class that scans through a folder with all of its subfolders and returns the following:
* Names and content of the unique files. "Unique" in this sense means, that if two files - `a.txt` and `b.tif` for example -
have the same content, only the first should be returned.
* Names of the "parent" files and their duplicates. In the example above, the parent file
is `a.txt`, since it was first in line, and its duplicate is `b.tif`.

```python
class FolderIterator:
    """ Iterates through the folder, finding duplicates """
    def __init__(self, foldername='./base'):
        self.foldername = ...  # pathlib.Path instance
        self.uniques = ...  # list instance
        self.duplicates = ...  # dict instance
        # Other attributes may follow

    def iter_folder(self):
        """
        Main function to find duplicate and unique files in the filesystem.
        Must use the "with" statement to open individual files.
        """

```

2. _Morse Code Interpreter:_
Write a program that reads a text file (`lorem.txt`), converts it to Morse code and writes it back
to a new file called `lorem_morse.txt`. In the new file, each (Morse) word should be in a new line.
Don't loop over the string. Rather, use built-in Python string methods to do the heavy lifting.



```python
MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

class EnglishToMorse:
    """ Convert a text file to Morse code file """

    # ...

    def convert(self):
        """ Convert self.file to one-word-in-line Morse and write it back to the disk """
```


## Tests
The tests for both questions are provided. Again, assignment grading is completely based on the success
of the tests. This type of tests is called _unit tests._ We'll
only discuss this concept later in the course, but we'll starting familiarizing ourselves with it right now.
The best testing library out there today is `pytest`, and so that's the library we'll use to
test our solution. By the way, the tests that I wrote for the previous assignment weren't really compatible
with the standard way people write tests, so don't make an example of them.

One of the things that makes `pytest` so good is its ease of use. To run the tests, open the terminal and download `pytest` using `pip`.
Don't forget to activate your environment before downloading. Next, navigate to the folder containing your code and verify
that the `test_qX.py` file is located in the same folder. Since this is a folder with Python source files, add in the
standard `__init__.py` file as well.

Now that we're all set up we can run the test. Inside that folder, write in the terminal `pytest`. It should recognize
the two `test_qX.py` files and run all tests in them consecutively, reporting back to you of any errors it encountered. If all tests in
all files run successfully you'll receive a perfect grade for the HW assignment.