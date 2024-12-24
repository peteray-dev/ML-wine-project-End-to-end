from mlproject.constants import *
from mlproject.utils.common import read_yaml, create_directories
from mlproject.entity.config_entity import DataIngestionConfig



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