from mlproject.logging import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline



STAGE_NAME = 'Data Ingestion stage'
try: 
    logger.info(f'>>>stage {STAGE_NAME} started >>>>>')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>stage one {STAGE_NAME} completed>>>>>>\n\nx===============')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data validation stage'
try: 
    logger.info(f'>>>stage {STAGE_NAME} started >>>>>')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>>stage {STAGE_NAME} completed>>>>>>\n\nx===============')

except Exception as e:
    logger.exception(e)
    raise e