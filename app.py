import sys
import os
import certifi
import pymongo
from dotenv import load_dotenv

load_dotenv()
ca=certifi.where()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import sys,os
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.pipeline.training_pipeline import TrainingPipeline
from network_security.utils.main_utils.util import load_object
from network_security.utils.ml_utils.model.estimator import NetworkModel
from fastapi import FastAPI,File,UploadFile,Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
from network_security.constant.training_pipeline import Data_Ingestion_Database,Data_Ingestion_Collection_name
database=client[Data_Ingestion_Database]
collection=client[Data_Ingestion_Collection_name]

app=FastAPI()
origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

from fastapi.templating import Jinja2Templates
templates=Jinja2Templates('./templates')
@app.get('/',tags=['authentication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get('/train')
async def train_route():
    try:
        obj=TrainingPipeline()
        obj.run_pipeline()
        return Response("Training Pipeline has been Runned")
    except Exception as e:
        raise NetworkSecurityException(e,sys)

@app.post('/predict')
async def predict_route(request:Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        preprocessor=load_object('final_models/preprocessor.pkl')
        model=load_object('final_models/model.pkl')
        
        obj=NetworkModel(preprocessor=preprocessor,model=model)
        y_hat=obj.get_predicted_val(df)

        print(y_hat)
        df['Predicted_Column']=y_hat
        table_html=df.to_html(classes='table table-striped')
        df.to_csv('predict_Output/predict.csv')
        return templates.TemplateResponse("table.html",{"request":request,"table":table_html})
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

if __name__=='__main__':
    app_run(app,host='localhost',port=8000)