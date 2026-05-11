from textSummarizer.utils.common import read_yaml, create_dir
from textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from textSummarizer.entity.__init__ import DataIngestionConfig, DataValidationConfig, DataTransformationConfig


class ConfigurationManager:
    def __init__(self,
                config_file_path=CONFIG_FILE_PATH,
                params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_dir([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            zip_dir=config.zip_dir
        )
        return data_ingestion_config
    


    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        create_dir([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
        return data_validation_config
    

    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation
        create_dir([config.root_dir])
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path, 
            tokenizer_name=config.tokenizer_name
        )
        return data_transformation_config


