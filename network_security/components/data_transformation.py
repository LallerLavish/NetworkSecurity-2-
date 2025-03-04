from network_security.entity.artifact_entity  import  DataValidationArtifact,DataTransformationArtifact
from network_security.entity.config_entity  import Data_Transformation_Configuration
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.constant import training_pipeline
from network_security.utils.main_utils.util import save_object,nump_to_file
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline

import sys,os
import pandas as pd
import numpy as np

class DataTransformation:
    def __init__(self,input_config:DataValidationArtifact,
                 transform_config:Data_Transformation_Configuration):
        self.input_config=input_config
        self.transform_config=transform_config

    def data_transforming(self,data:pd.DataFrame,params:dict):
         try:
            numerical_columns=data.columns
            num_pipeline=Pipeline([
                ('imputer',KNNImputer(missing_values=list(params.values())[0],
                                    n_neighbors=list(params.values())[1],
                                    weights=list(params.values())[2])),
                ('scaler',RobustScaler())
            ])
            
            preprocessor=ColumnTransformer([
                ("num",num_pipeline,numerical_columns)
            ])

            return preprocessor
         except Exception as e:
             raise NetworkSecurityException(e,sys)

    def initiate_Transformation(self)->DataTransformationArtifact:
        try:
            train_file_path=self.input_config.valid_train_file_path
            test_file_path=self.input_config.valid_test_file_path

            train_csv=pd.read_csv(train_file_path)
            test_csv=pd.read_csv(test_file_path)

            train_target=train_csv[training_pipeline.Target_column]
            train_target=train_target.replace(-1,0)
            train_csv=train_csv.drop(training_pipeline.Target_column,axis=1)

            test_target=test_csv[training_pipeline.Target_column]
            test_target=test_target.replace(-1,0)
            test_csv=test_csv.drop(training_pipeline.Target_column,axis=1)

            preprocessor=self.data_transforming(train_csv,training_pipeline.Data_NAN_Replacer_params)

            train_tr=preprocessor.fit_transform(train_csv)
            test_tr=preprocessor.transform(test_csv)

            train_arr=np.c_[train_tr,np.array(train_target)]
            test_arr=np.c_[test_tr,np.array(test_target)]

            save_object(self.transform_config.data_transformer_obj,preprocessor)
            nump_to_file(self.transform_config.data_trans_train,train_arr)
            nump_to_file(self.transform_config.data_trans_test,test_arr)

            data_tranformer_artifact=DataTransformationArtifact(
                transformed_test_file_path=self.transform_config.data_trans_test,
                transformed_train_file_path=self.transform_config.data_trans_train,
                transformed_object_file_path=self.transform_config.data_transformer_obj
            )
            return data_tranformer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)