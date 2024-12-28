from mlproject.constants import *
from mlproject.utils.common import read_yaml, create_directories
from mlproject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig



class ConfigurationManager:
    def __init__(self, 
                 config_pathway=CONFIG_FILE_PATH, 
                 param_pathway=PARAM_FILE_PATH, 
                 schema_pathway=SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_pathway)
        self.param = read_yaml(param_pathway)
        self.schema = read_yaml(schema_pathway)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            Source_URL= config.Source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self)-> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema= schema,
        )
            
        return data_validation_config
    

    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config

    def get_model_trainer_config(self):
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN
        params = self.param.ElasticNet

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config
    
# for src configuration for validation
# class ConfigurationManager:
#     def __init__(self, 
#                  config_pathway=CONFIG_FILE_PATH, 
#                  param_pathway=PARAM_FILE_PATH, 
#                  schema_pathway=SCHEMA_FILE_PATH):
        
#         self.config = read_yaml(config_pathway)
#         self.param = read_yaml(param_pathway)
#         self.schema = read_yaml(schema_pathway)

#         create_directories([self.config.artifacts_root])

    