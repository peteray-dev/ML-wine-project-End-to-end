import os
import pandas as pd
# from mlproject.logging import logger
from mlproject.config.configuration import DataValidationConfig


class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'validation status for columns {validation_status}')

                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'validation status for columns {validation_status}')

                return validation_status

        except Exception as e:
            # logger.exception(e)
            raise e
        

    def validate_all_datatypes(self) -> bool:
        try:
            validation_status = None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_datatypes = list(data.dtypes)

            all_schema_datatypes = self.config.all_schema.values()

            for datatype in all_datatypes:
                # actual_datatype = data[col].dtype
                if datatype not in all_schema_datatypes:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f'\n validation status for data types {validation_status}')

                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f'\n validation status for data types {validation_status}')

                return validation_status

        except Exception as e:
            # logger.exception(e)
            raise e