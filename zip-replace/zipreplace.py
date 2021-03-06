from pathlib import Path
import zipfile
import shutil
import sys
from create_test_zip_file import gen_test_zip_file
from zipprocessor import ZipProcessor


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_dir = Path('unzipped-{}'.format(filename))

    def zip_file_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_dir.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_dir))

    def find_replace(self):
        for filename in self.temp_dir.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)

            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_dir.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_dir))


if __name__ == '__main__':
    ZipReplace(*sys.argv[1:4]).zip_file_replace()
    # gen_test_zip_file()
    # ZipReplace(filename='testfile.zip', search_string='hello', replace_string='xin chao')
