import yaml
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
import os,sys
import dill
import pickle
import numpy as np

def read_yaml_file(file_path):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def write_yaml_file(file_path:str,content:object,replace:bool):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
            
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def nump_to_file(file_path:str,array:np.ndarray):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file:
            np.save(file,array)
        logging.info("File is saved")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_object(file_path:str,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file:
            pickle.dump(obj,file)
        logging.info("Object(Preprocessor) is Saved")

    except Exception as e:
        raise NetworkSecurityException(e,sys)
