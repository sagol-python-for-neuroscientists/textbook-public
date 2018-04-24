"""
__author__ = Hagai Har-Gil
"""
import pathlib


class FolderIterator:
    """ Iterates through the folder, finding duplicates """
    def __init__(self, foldername='./base'):
        self.foldername = pathlib.Path(str(foldername))
        assert self.foldername.exists()
        self.uniques = []  # list of tuples of (filename, content)
        self.duplicates = {}
        self.content = []

    def iter_folder(self):
        """
        Main function to find duplicate and unique files in the filesystem.
        Must use the "with" statement.
        """

        for file in self.foldername.rglob('*.*'):
            with open(file, 'r') as f:
                content = f.read()
            if content in self.content:
                for item in self.uniques:
                    if item[1] == content:
                        self.duplicates[item[0]].append(str(file))

            else:
                self.content.append(content)
                self.uniques.append((str(file), content))
                self.duplicates[str(file)] = []


if __name__ == '__main__':
    fol = FolderIterator()
    fol.iter_folder()
    print(fol.uniques)
    print(fol.duplicates)
