# Homework Assignment #3

## Date: 01-04-2019
## Due date: 15-04-2019, 15:00

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
        pass

```

The folder in question is `base`, also located in this repo.

2. _Morse Code Interpreter:_
Write a program that reads a text file (`lorem.txt`), converts it to Morse code and writes it back
to a new file called `lorem_morse.txt`. In the new file, each (Morse) word should be in a new line.
**Don't loop over the string.** Rather, use built-in Python string methods to do the _heavy lifting_.


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
w '-....-',
w
w
class EnglishToMorse:
    """ Convert a text file to Morse code file """
    def __init__(self, file):
        self.file = ...
        # ...

    def convert(self):
        """ Convert self.file to one-word-in-line Morse """

    def to_disk(self, fname='lorem_morse.txt'):
        """ Writes data to the disk with filename == fname """

```


3. _Basic `numpy` Calculations:_

    Saving and loading `numpy` arrays is done using the functions `np.load`, `np.save` and `np.savez`. A single array is saved in the `.npy` format using `np.save`, while a dictionary of arrays is saved to the `.npz` format using `np.savez`. Both data structures can be read using `np.load`. In the repo you can see `data.npy`, a single 4D array that I randomly generated. The file `hw3_q3.py` should contain functions that take this specific array as input.

    i. Define the `load_data` function which receives a filename and returns the array.

    ```python
    def load_data(fname: str):
        """ Load and return an '.npy' file """
    ```

    ii. Find and return all numbers within the range (0.3, 0.4) in the array. Note: exclusive on both ends.

    ```python
    def find_in_range(data: np.ndarray, num_range: tuple=(0.3, 0.4)):
        """ Return an array containing the values of 'data' that are inside 'num_range' """
    ```

    iii. Return the index of the first value larger than 0.9, the input value. The index is a
    `numpy` array with one dimension and four values, which are the coordinates at which one can find
    this value. Meaing that the line `data[returned_index]` returns the first value above 0.9.

    ```python
    def first_after_val(data: np.ndarray, val: float=0.9) -> np.ndarray:
        """ Return the position of the first value larger than val """
    ```

## Tests
The tests for both questions are provided. Again, assignment grading is completely based on the success
of the tests, for all three questions.