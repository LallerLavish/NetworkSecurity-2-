from network_security.constant import training_pipeline
import os
import sys
from datetime import datetime

class Training_Pipeline_Config:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.pipeline=training_pipeline.Pipeline_name
        self.artifact_name=training_pipeline.Artifacts_dir
        self.artifact_path=os.path.join(self.artifact_name,timestamp)
        self.timestamp=timestamp

class Data_Ingestion_Configuration:
    def __init__(self,train_pip_confi=Training_Pipeline_Config):
        self.data_ingestion_dir=os.path.join(train_pip_confi.artifact_path,
                                             training_pipeline.Data_Ingestion_dir_name)
        self.feature_store_path=os.path.join(self.data_ingestion_dir,
                                             training_pipeline.Data_Ingestion_feature_store,
                                             training_pipeline.Data_file_name)
        self.test_path=os.path.join(self.data_ingestion_dir,
                                    training_pipeline.Data_Ingestion_ingested_dir,
                                    training_pipeline.Test_file_name)
        self.train_path=os.path.join(self.data_ingestion_dir,
                                     training_pipeline.Data_Ingestion_ingested_dir,
                                     training_pipeline.Train_file_name)
        self.test_train_split_ratio:float=training_pipeline.Data_Ingestion_train_test_split_ratio
        self.collection=training_pipeline.Data_Ingestion_Collection_name
        self.database=training_pipeline.Data_Ingestion_Database

class Data_Validation_Configuration:
    def __init__(self,train_pip_confi=Training_Pipeline_Config):
        self.data_valid_dir=os.path.join(train_pip_confi.artifact_path,
                                         training_pipeline.Data_Validation_dir_name)
        self.valid_dir=os.path.join(self.data_valid_dir,
                                    training_pipeline.Data_Validation_valid_dir)
        self.invalid_dir=os.path.join(self.data_valid_dir,
                                    training_pipeline.Data_Validation_invalid_dir)
        self.valid_train_file_path=os.path.join(self.valid_dir,training_pipeline.Train_file_name)
        self.valid_test_file_path=os.path.join(self.valid_dir,training_pipeline.Test_file_name)
        self.invalid_train_file_path=os.path.join(self.invalid_dir,training_pipeline.Train_file_name)
        self.invalid_test_file_path=os.path.join(self.invalid_dir,training_pipeline.Test_file_name)
        self.drift_report_file_path=os.path.join(self.data_valid_dir,
                                                 training_pipeline.Data_Validation_drift_report_dir,
                                                 training_pipeline.Data_Validation_drift_report_name)

class Data_Transformation_Configuration:
    def __init__(self,tpc:Training_Pipeline_Config):
        self.train_pip_confi=tpc
        self.data_transformer=os.path.join(self.train_pip_confi.artifact_path,training_pipeline.Data_Transformation_dir_name)
        self.data_trans_train=os.path.join(self.data_transformer,training_pipeline.Train_file_name.replace("csv","npy"))
        self.data_trans_test=os.path.join(self.data_transformer,training_pipeline.Test_file_name.replace("csv","npy"))
        self.data_transformer_obj=os.path.join(self.data_transformer,training_pipeline.PREPROCESSOR_FILE_NAME)

class Model_Training_Configuration:
    def __init__(self,train_pip_confi:Training_Pipeline_Config):
        self.train_pip_config=train_pip_confi
        self.model_train_dir_path=os.path.join(self.train_pip_config.artifact_path,
                                               training_pipeline.Model_Trainer_dir_name)
        self.model_file_path=os.path.join(self.model_train_dir_path,training_pipeline.MODEL_FILE_NAME)
        self.expected_accuracy:float=training_pipeline.Model_Expected_Accuracy
        self.model_under_overfitted_threshold=training_pipeline.Model_underfitting_overfitting_threshold
