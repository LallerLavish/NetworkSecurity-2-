import os
import sys
import pandas as pd
import numpy as np


"""
defining common constants for pipeline
"""
Target_column="Result"
Pipeline_name="NetworkSecurity"
Artifacts_dir="Artifacts"
Data_file_name="phisingData.csv"

Test_file_name="test.csv"
Train_file_name="train.csv"
SCHEMA_FILE_PATH="data_schema/schema.yaml"

"""
Data Ingestion Related Constant
"""

Data_Ingestion_Collection_name:str="network_data"
Data_Ingestion_Database:str="networkDataBase"
Data_Ingestion_dir_name:str="data_ingestion"
Data_Ingestion_feature_store:str="feature_store"
Data_Ingestion_ingested_dir:str="ingested_data"
Data_Ingestion_train_test_split_ratio:float=0.2

"""
Data Validation Related Constants 
"""

Data_Validation_dir_name:str="Data_Validation"
Data_Validation_valid_dir:str="Valid"
Data_Validation_invalid_dir:str="Invalid"
Data_Validation_drift_report_dir:str="Drift_Report"
Data_Validation_drift_report_name:str="report.yaml"