import zipfile
from pathlib import Path
import os

def gen_test_zip_file():
    _create_test_text_files()

    zipped_file = "testfile.zip"

    with zipfile.ZipFile(zipped_file, mode="w") as file:
        for filename in [str(filename) for filename in Path('.').iterdir() \
                         if str(filename).startswith('file') and str(filename).endswith('.txt')]:
            file.write(filename)
            os.remove(filename)


def _create_test_text_files():
    content1 = "bla bla file1 hello bla"
    file1 = Path("file1.txt")

    with file1.open("w") as file:
        file.write(content1)

    # content2 = "bla bla file1 good morning bla"
    # file2 = Path("file2.txt")
    # with file2.open("w") as file:
    #     file.write(content2)


if __name__ == '__main__':
    gen_test_zip_file()