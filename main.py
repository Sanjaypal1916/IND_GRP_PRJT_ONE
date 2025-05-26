import sys
sys.path.append("c:/Users/sanjay/Desktop/AI ML/ML-Projects/IND_GRD_PROJECT_ONE/src")
from DataScience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from DataScience.utils.commons import read_yaml, create_directory
from DataScience.pipeline.dataIngestionPipeline import dataIngestionPipeline




STAGE_NAME = "Data Ingestion stage"
try:
   data_ingestion_pipe = dataIngestionPipeline()
   data_ingestion_pipe.initialize_data_ingestion()
   print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        print(e)
        raise e
