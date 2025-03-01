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
