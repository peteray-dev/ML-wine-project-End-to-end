from mlproject.config.configuration import ConfigurationManager
from mlproject.component.data_transformation import DataTransformation
from mlproject.logging import logger
from pathlib import Path

STAGE_NAME = "Data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
                # print(f'the status is {status}')

            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception(" Your Schema is Invalid")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>stage one {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger.exception(e)
        raise e