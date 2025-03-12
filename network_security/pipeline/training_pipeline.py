from network_security.components.data_ingestion import Data_Ingestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.components.model_trainer import ModelTrainer

from network_security.entity.config_entity import (
    Training_Pipeline_Config,
    Data_Ingestion_Configuration,
    Data_Validation_Configuration,
    Data_Transformation_Configuration,
    Model_Training_Configuration
)

from network_security.entity.artifact_entity import(
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact
)

import sys,os
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

class TrainingPipeline:
    def __init__(self):
        self.training_pip_config=Training_Pipeline_Config()
    
    def start_data_ingest(self):
        try:
            logging.info("Data ingestion has started")
            data_ingest=Data_Ingestion(Data_Ingestion_Configuration(self.training_pip_config))
            data_ingest_artifact=data_ingest.initiate_data_ingestion()
            logging.info("Data ingestion has completed")
            logging.info(f"Data artifact: {data_ingest_artifact}")
            return data_ingest_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_data_validation(self,ingested_data:DataIngestionArtifact):
        try:
            logging.info("Data validation has started")
            data_validated=DataValidation(Data_Validation_Configuration(self.training_pip_config),ingested_data)
            data_validated_artifact=data_validated.initiate_data_validation()
            logging.info("Data validation has completed")
            logging.info(f"Validated artifact: {data_validated_artifact}")
            return data_validated_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_data_transform(self,validated_data:DataValidationArtifact):
        try:
            logging.info("Data transformation has started")
            data_transform=DataTransformation(validated_data,Data_Transformation_Configuration(self.training_pip_config))
            data_transform_artifact=data_transform.initiate_Transformation()
            logging.info("Data transformation has completed")
            logging.info(f"Transformed artifact: {data_transform_artifact}")
            return data_transform_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_model_training(self,transformed_data:DataTransformationArtifact):
        try:
            logging.info("Data ingestion has started")
            data_model_trained=ModelTrainer(transformed_data,Model_Training_Configuration(self.training_pip_config))
            data_model_trained_artifact=data_model_trained.initiateTraining()
            logging.info("Data model_training has completed")
            logging.info(f"Data artifact: {data_model_trained_artifact}")
            return data_model_trained_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            input1=self.start_data_ingest()
            input2=self.start_data_validation(input1)
            input3=self.start_data_transform(input2)
            return self.start_model_training(input3)
        except Exception as e:
            raise NetworkSecurityException(e,sys)