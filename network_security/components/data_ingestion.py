import pymongo.mongo_client
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import Data_Ingestion_Configuration
from network_security.entity.artifact_entity import DataIngestionArtifact

from sklearn.model_selection import train_test_split

import pymongo 
import pymongo.mongo_client

import sys
import numpy as np
import pandas as pd
from typing import List
import os


from dotenv import load_dotenv
load_dotenv()

MONGO_URL=os.getenv("MONGO_DB_URL")

class Data_Ingestion:
    def __init__(self,confi=Data_Ingestion_Configuration):
        try:
            self.confi=confi
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def load_data(self):
        try:    
            self.client=pymongo.MongoClient(MONGO_URL)
            database=self.confi.database
            collection=self.confi.collection

            databS=self.client[database][collection]
            df=pd.DataFrame(list(databS.find()))
            
            if "_id" in df.columns:
                df.drop("_id",axis=1,inplace=True)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def data_to_featueStore(self,dataframe:pd.DataFrame):
        feature_store_file_path=self.confi.feature_store_path
        dir_path=os.path.dirname(feature_store_file_path)
        os.makedirs(dir_path,exist_ok=True)
        dataframe.to_csv(feature_store_file_path,index=False,header=True)
        return dataframe
    
    def split_dataset(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.confi.test_train_split_ratio,random_state=42)
            logging.info("Data is splitted in test and train")

            train_set_path=self.confi.train_path
            dir_path=os.path.dirname(train_set_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exporting train and test set")

            train_set.to_csv(self.confi.train_path,index=False,header=True)

            test_set.to_csv(self.confi.test_path,index=False,header=True)

            logging.info("Splitting and Exporting Completed Successfully")
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_ingestion(self):
        try:
            data=self.load_data()
            logging.info("Data is loaded from mongoAtlas")
            data=self.data_to_featueStore(data)
            logging.info("data is put into feature store")

            logging.info("splitting has started")

            self.split_dataset(data)

            dataingestionartifact=DataIngestionArtifact(
                train_path=self.confi.train_path,
                test_path=self.confi.test_path
            )

            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)