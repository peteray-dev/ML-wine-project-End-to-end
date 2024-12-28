from mlproject.config.configuration import ConfigurationManager
from mlproject.component.model_evaluation import ModelEvaluation
from mlproject.logging import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_result()



if __name__ == '__main__':
    try:
        logger.info(f'>>>stage {STAGE_NAME} started >>>>>')
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>>>>stage {STAGE_NAME} completed>>>>>>\n\nx===============')

    except Exception as e:
        logger.exception(e)
        raise e
