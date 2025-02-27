import os
import sys
import json

import pymongo.mongo_client
from network_security.logging.logger import logging
from network_security.exception.exception import NetworkSecurityException
import pandas as pd
import numpy as np
import pymongo 

from dotenv import load_dotenv 
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

import certifi
ca=certifi.where()

class DataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,path):
        try:
            data=pd.read_csv(path)
            data.reset_index(drop=True,inplace=True)
            records=data.to_dict(orient="records")
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_mongo(self,records,database,collection):
        try:
            self.records=records
            self.database=database
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH="network_data/phisingData.csv"
    DATABASE="networkDataBase"
    COLLECTION="network_data"
    network_obj=DataExtract()
    records=network_obj.csv_to_json(FILE_PATH)
    no_of_records=network_obj.insert_mongo(records,DATABASE,COLLECTION)
    print(no_of_records)