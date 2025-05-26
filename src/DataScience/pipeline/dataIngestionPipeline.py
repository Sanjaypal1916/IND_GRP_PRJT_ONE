import sys
sys.path.append("c:/Users/sanjay/Desktop/AI ML/ML-Projects/IND_GRD_PROJECT_ONE/src")
from DataScience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from DataScience.utils.commons import read_yaml, create_directory
from DataScience.entity.config_entity import dataIngestionConfig
from DataScience.config.configuration import configurationmanager
from DataScience.components.dataIngestion import data_ingestion

class dataIngestionPipeline():

    STAGE_NAME = "DATA INGESTION PIPELINE"
    def initialize_data_ingestion(self):
        try:
            config = configurationmanager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion_ = data_ingestion(config = data_ingestion_config)
            data_ingestion_.download_file()
            data_ingestion_.unzip_file()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<< THE WORK GOT OVER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        except Exception as e :
            raise e