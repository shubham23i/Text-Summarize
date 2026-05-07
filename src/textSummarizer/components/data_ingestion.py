import os
from urllib import request
import urllib
from zipfile import ZipFile
from textSummarizer.logging import logger
from textSummarizer.exception import CustomException
from textSummarizer.utils.common import get_size
from textSummarizer.entity.__init__ import DataIngestionConfig
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=urllib.request.urlretrieve(self.config.source_url,self.config.local_data_file)
            logger.info(f"{filename} downlaaded successfully with info {headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists")


    def extract_zip_file(self):
        print("Entered extract_zip_file")
        unzip_path=self.config.zip_dir
        os.makedirs(unzip_path,exist_ok=True)
        file_path = self.config.local_data_file

        
        with ZipFile(self.config.local_data_file) as zip_file:
            zip_file.extractall(unzip_path)
            logger.info(f"Zip file {self.config.local_data_file} extracted successfully")
