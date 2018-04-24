"""
__author__ = Hagai Har-Gil
"""
import pathlib
import os


class EnglishToMorse:
    """ Convert a text file to Morse code file using numpy """
    def __init__(self, file):
        self.file = pathlib.Path(str(file))
        assert self.file.exists()

        CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
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

                ' ': '\n', '.': '.-.-.-', ',': '--..--',
                ':': '---...', "'": '.----.', '-': '-....-',
                }
        code_ord_upper = {ord(key): val for key, val in CODE.items()}
        code_ord_lower = {ord(key.lower()): val for key, val in CODE.items()}

        self.new_code = {**code_ord_lower, **code_ord_upper}
        self.data = None

    def convert(self):
        """ Convert self.file to Morse and write it back to the disk """
        with open(self.file) as f:
            data = f.read()
        self.data = data.translate(self.new_code)
        split = os.path.splitext(self.file.name)
        new_filename = split[0] + '_morse' + split[1]
        with open(new_filename, 'w') as f:
            f.write(self.data)


if __name__ == '__main__':
    morse = EnglishToMorse('lorem.txt')
    morse.convert()
