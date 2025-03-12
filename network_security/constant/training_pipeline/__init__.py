import os
import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

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
PREPROCESSOR_FILE_NAME="preprocessor.pkl"
MODEL_FILE_NAME="model.pkl"
models:dict={
    
    'DecisionTree':DecisionTreeClassifier(),
    'RandomForest':RandomForestClassifier(verbose=0),
    'Gradient':GradientBoostingClassifier(verbose=0),
    'Logistic':LogisticRegression(verbose=0),
    'AdaBoost':AdaBoostClassifier()
    
}

params:dict={
            "Decision Tree": {
                'criterion':['gini', 'entropy', 'log_loss'],
                # 'splitter':['best','random'],
                # 'max_features':['sqrt','log2'],
            },
            "Random Forest":{
                # 'criterion':['gini', 'entropy', 'log_loss'],
                
                # 'max_features':['sqrt','log2',None],
                'n_estimators': [8,16,32,128,256]
            },
            "Gradient Boosting":{
                # 'loss':['log_loss', 'exponential'],
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.85,0.9],
                # 'criterion':['squared_error', 'friedman_mse'],
                # 'max_features':['auto','sqrt','log2'],
                'n_estimators': [8,16,32,64,128,256]
            },
            "Logistic Regression":{},
            "AdaBoost":{
                'learning_rate':[.1,.01,.001],
                'n_estimators': [8,16,32,64,128,256]
            }
            
        }

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

"""
Data Transformation Related Constants
"""

Data_Transformation_dir_name:str="Data_Transformer"
# KNN Imputer
Data_NAN_Replacer_params:dict={
    'missing_values':np.nan,
    'n-_neighbors':3,
    'weights':'uniform'
}

"""
Model Trainer Related Constants
"""

Model_Trainer_dir_name:str="Model_Trainer"
Model_Expected_Accuracy:float=0.6
Model_underfitting_overfitting_threshold=0.05

Training_Bucket_Name="lavishnetworksecurity"