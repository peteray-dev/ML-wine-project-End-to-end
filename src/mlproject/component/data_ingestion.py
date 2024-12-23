#data ingestion component
from pathlib import Path
import os
import zipfile
import urllib.request as request
from mlproject.logging import logger
from mlproject.utils.common import get_size
from mlproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.Source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f'{filename} downloaded! with following info \n{headers}')

        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: zip
        extract zip file into the directory
        function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)