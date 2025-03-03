from network_security.entity.artifact_entity  import  DataValidationArtifact
from network_security.entity.artifact_entity  import  DataIngestionArtifact
from network_security.entity.config_entity  import Data_Validation_Configuration
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.constant import training_pipeline
from network_security.utils.main_utils.util import read_yaml_file
from network_security.utils.main_utils.util import write_yaml_file
import sys,os
from scipy.stats import ks_2samp
import pandas as pd
import numpy as np


class DataValidation:
    def __init__(self,valid_config:Data_Validation_Configuration
                 ,ingest_config:DataIngestionArtifact):
        self.validation_config=valid_config
        self.ingest_config=ingest_config
        self.schema_config=read_yaml_file(training_pipeline.SCHEMA_FILE_PATH)

    def validate_num_of_cols(self,dataframe:pd.DataFrame)->bool:
        try:
            no_of_cols=len(self.schema_config["columns"])
            logging.info("Checking for equal num of columns")
            return no_of_cols==len(dataframe.columns)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def validate_numerical_cols(self,dataframe:pd.DataFrame)->bool:
        try:
            list1=self.schema_config["numerical_columns"]
            for i in (list1):
                if dataframe[i].dtype == object:
                    return False

            return True 
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def detect_drift_change(self,curr_df:pd.DataFrame,prev_df:pd.DataFrame,threshold=0.05):
        try:
            status=True
            report={}
            for i in curr_df.columns:
                s1=curr_df[i]
                s2=prev_df[i]
                val=ks_2samp(s1,s2)
                if val.pvalue>=threshold:
                    isFound=False
                else:
                    isFound=True
                    status=False
                
                report.update({i:{
                        "p_value":float(val.pvalue),
                        "drift_status":isFound
                }})
            drift_report_file_path=self.validation_config.drift_report_file_path
            write_yaml_file(file_path=drift_report_file_path,content=report,replace=False)

            return status


        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            logging.info("Validation of the Data has been Started")
            test_file=pd.read_csv(self.ingest_config.test_path)
            train_file=pd.read_csv(self.ingest_config.train_path)

            status_train1=self.validate_num_of_cols(train_file)
            status_test1=self.validate_num_of_cols(test_file)
            
            status_train2=self.validate_numerical_cols(train_file)
            status_test2=self.validate_numerical_cols(test_file)

            status_drift=self.detect_drift_change(curr_df=train_file,prev_df=test_file)

            if(status_train1 and status_train2):
                os.makedirs(os.path.dirname(self.validation_config.valid_train_file_path),exist_ok=True)
                train_file.to_csv(self.validation_config.valid_train_file_path,index=False,header=True)
            else:
                print("Train DataFrame data validation Failed")
            
            if(status_test1 and status_test2):
                os.makedirs(os.path.dirname(self.validation_config.valid_test_file_path),exist_ok=True)
                test_file.to_csv(self.validation_config.valid_test_file_path,index=False,header=True)
            else:
                print("Test DataFrame data validation Failed")


            artifact_Validation=DataValidationArtifact(
                validation_status=status_drift and status_test1 and status_train1 and status_test2 and status_train2,
                valid_train_file_path=self.ingest_config.train_path,
                valid_test_file_path=self.ingest_config.test_path,
                invalid_test_file_path=None,
                invalid_train_file_path=None,
                drift_report_file_path=self.validation_config.drift_report_file_path
            )
            return artifact_Validation
        except Exception as e:
            raise NetworkSecurityException(e,sys)