import os
import urllib.request as request
import zipfile



class data_ingestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_dir):
            filename , header = request.urlretrieve( filename = self.config.local_data_dir, url = self.config.source_url)
            print("file downloaded")
        else:
            print("file already exists")


    def unzip_file(self):

        os.makedirs(self.config.unzip_data_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_dir, "r") as f:
            f.extractall(self.config.unzip_data_dir)
        print("unzipped the file ")
