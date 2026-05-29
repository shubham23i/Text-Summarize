import os
import sys

sys.path.append(os.path.abspath("src"))

from textSummarizer.logging import logger
from textSummarizer.exception import CustomException

from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from textSummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)
from textSummarizer.pipeline.stage_04_model_trainer import (
    ModelTrainingPipeline,
)
from textSummarizer.pipeline.stage_05_model_evaluation import (
    ModelEvaluationPipeline,
)


def run_stage(stage_name, pipeline_obj):
    try:
        logger.info(f">>>>>>> {stage_name} started <<<<<<<")

        pipeline = pipeline_obj()
        pipeline.main()

        logger.info(f">>>>>>> {stage_name} completed <<<<<<<\n")

    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)


if __name__ == "__main__":

    run_stage(
        "DATA INGESTION STAGE",
        DataIngestionTrainingPipeline
    )

    run_stage(
        "DATA VALIDATION STAGE",
        DataValidationTrainingPipeline
    )

    run_stage(
        "DATA TRANSFORMATION STAGE",
        DataTransformationTrainingPipeline
    )

    run_stage(
        "MODEL TRAINING STAGE",
        ModelTrainingPipeline
    )

    run_stage(
        "MODEL EVALUATION STAGE",
        ModelEvaluationPipeline
    )