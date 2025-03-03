from network_security.components.data_ingestion import Data_Ingestion
from network_security.components.data_validation import DataValidation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import Training_Pipeline_Config,Data_Ingestion_Configuration,Data_Validation_Configuration
from network_security.entity.artifact_entity import DataIngestionArtifact
import sys

if __name__=="__main__":
    try:
        data_ing=Data_Ingestion(Data_Ingestion_Configuration(Training_Pipeline_Config()))
        data_artifact=data_ing.initiate_data_ingestion()
        print(data_artifact)

        validated_obj=DataValidation(Data_Validation_Configuration(Training_Pipeline_Config()),data_artifact)
        validated_artifact=validated_obj.initiate_data_validation()
        print(validated_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)