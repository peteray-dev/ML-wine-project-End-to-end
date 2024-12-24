from mlproject.config.configuration import ConfigurationManager
from mlproject.component.data_validation import DataValidation
from mlproject.logging import logger

STAGE_NAME = "Data validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_all_datatypes()

        
if __name__ == '__main__':
    try:
        logger.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>stage one {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger.exception(e)
        raise e