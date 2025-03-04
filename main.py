from network_security.components.data_ingestion import Data_Ingestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import Training_Pipeline_Config,Data_Ingestion_Configuration,Data_Validation_Configuration,Data_Transformation_Configuration
from network_security.entity.artifact_entity import DataIngestionArtifact
import sys

if __name__=="__main__":
    try:
        logging.info("Data Ingestion Started")
        data_ing=Data_Ingestion(Data_Ingestion_Configuration(Training_Pipeline_Config()))
        data_artifact=data_ing.initiate_data_ingestion()
        print(data_artifact)
        logging.info("Data Ingestion Completed")
        logging.info("Data Validation Started")
        validated_obj=DataValidation(Data_Validation_Configuration(Training_Pipeline_Config()),data_artifact)
        validated_artifact=validated_obj.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(validated_artifact)
        logging.info("Data Transformation Started")
        transform=DataTransformation(validated_artifact,Data_Transformation_Configuration(Training_Pipeline_Config()))
        transformed_obj=transform.initiate_Transformation()
        logging.info("Data Transformation Completed")
        print(transformed_obj)

    except Exception as e:
        raise NetworkSecurityException(e,sys)