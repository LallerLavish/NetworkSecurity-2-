from network_security.entity.artifact_entity  import  ModelTrainerArtifact,DataTransformationArtifact
from network_security.entity.config_entity  import Model_Training_Configuration
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.constant import training_pipeline
from network_security.utils.main_utils.util import save_object,load_numpy_file,load_object
from network_security.utils.ml_utils.metric.classification_metric import get_classification_report,ClassificationMetricReport
from network_security.utils.ml_utils.model.estimator import NetworkModel
from sklearn.model_selection import GridSearchCV
import mlflow
import dagshub
dagshub.init(repo_owner='LallerLavish', repo_name='my-first-repo', mlflow=True)

import pandas as pd
import numpy as np
import os,sys

class ModelTrainer:
    def __init__(self,transform_config:DataTransformationArtifact,
                 model_config:Model_Training_Configuration):
        self.transform_config=transform_config
        self.model_config=model_config

    def track_flow(self,model,classificationMetrics:ClassificationMetricReport):
        try:
            with mlflow.start_run():
                f1_score=classificationMetrics.f1_score
                recall_score=classificationMetrics.recall
                precision_score=classificationMetrics.precision
            
                mlflow.log_metric('f1_score',f1_score)
                mlflow.log_metric('recall_score',recall_score)
                mlflow.log_metric('precision',precision_score)
                
                mlflow.sklearn.log_model(model,'best_model')

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def train_model(self,X,y,X_test,y_test)->ModelTrainerArtifact:
        try:
            logging.info("model is getting trained")
            models:dict=training_pipeline.models
            params:dict=training_pipeline.params
            model_list=list(models.values())
            params_list=list(params.values())
            final_report:dict={}
            logging.info("Model Training has started")
            for i in range(len(model_list)):
                model=model_list[i]
                param=params_list[i]
                grid_model=GridSearchCV(estimator=model,cv=3,param_grid=param,verbose=0)
                grid_model.fit(X,y)

                model.set_params(**grid_model.best_params_)
                model.fit(X,y)
                y_hat=model.predict(X_test)
                report=get_classification_report(y_test,y_hat)
                final_report[list(models.keys())[i]]=report.f1_score
                
            best_val=max(sorted(list(final_report.values())))
            best_model_name=list(final_report.keys())[list(final_report.values()).index(best_val)]

            best_model=models[best_model_name]

            os.makedirs(os.path.dirname(self.model_config.model_file_path),exist_ok=True)
            save_object(self.model_config.model_file_path,best_model)

            save_object('final_models/model.pkl',best_model)
            
            print(get_classification_report(y_test,best_model.predict(X_test)))
            self.track_flow(best_model,get_classification_report(y_test,best_model.predict(X_test)))
            self.track_flow(best_model,get_classification_report(y,best_model.predict(X)))
            training_artifact=ModelTrainerArtifact(
                model_trained_file_path=self.model_config.model_file_path
            )
            logging.info("Model has been trained")
            return training_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def initiateTraining(self):
        train_data=load_numpy_file(self.transform_config.transformed_train_file_path)
        test_data=load_numpy_file(self.transform_config.transformed_test_file_path)

        X_train,y_train,X_test,y_test=(
            train_data[:,:-1],
            train_data[:,-1],
            test_data[:,:-1],
            test_data[:,-1]
        )

        trained_model_artifact=self.train_model(X_train,y_train,X_test,y_test)

        return trained_model_artifact

