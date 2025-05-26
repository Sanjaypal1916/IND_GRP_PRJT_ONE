import sys
sys.path.append("c:/Users/sanjay/Desktop/AI ML/ML-Projects/IND_GRD_PROJECT_ONE/src")
from DataScience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from DataScience.utils.commons import read_yaml, create_directory
from DataScience.entity.config_entity import dataIngestionConfig

class configurationmanager:
    def __init__(self,  
                config_filepath= CONFIG_FILE_PATH, 
                params_filepath = PARAMS_FILE_PATH, 
                schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath) 
        self.params =  read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directory([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> dataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion_config = dataIngestionConfig(
            root_dir = config.root_dir, 
            source_url= config.source_url,  
            local_data_dir = config.local_data_dir, 
            unzip_data_dir = config.unzip_data_dir
        )

        return data_ingestion_config


