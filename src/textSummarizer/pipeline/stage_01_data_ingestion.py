from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.__init__ import DataIngestion
from textSummarizer.logging import logger
from textSummarizer.exception import CustomException


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException(e,sys)