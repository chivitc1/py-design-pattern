import shutil
import zipfile
from pathlib import Path

"""
Abstract zip file processing, never use it directly in app
"""
class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_dir = Path('unzipped-{}'.format(zipname[:-4]))

    def process_zip(self):
        """
        Action with zip file like: search-replace text, scale images,...
        :return:
        """
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_dir.mkdir()
        with zipfile.ZipFile(file=self.zipname, mode='r') as zip:
            zip.extractall(str(self.temp_dir))

    def zip_files(self):
        with zipfile.ZipFile(file=self.zipname, mode='w') as zip:
            for filename in self.temp_dir.iterdir():
                zip.write(filename=str(filename), arcname=filename.name)
        shutil.rmtree(str(self.temp_dir))
