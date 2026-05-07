from textSummarizer.logging import logger
from textSummarizer.exception.__init__ import CustomException
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
import sys


STAGE_NAME="DATA INGESTION STAGE"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<<<")
except Exception as e:  
    raise CustomException(e,sys)


STAGE_NAME="DATA VALIDATION STAGE"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<<<")
except Exception as e:  
    raise CustomException(e,sys)

