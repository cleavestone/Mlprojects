import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score



def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file:
            pickle.dump(obj,file)

    except Exception as e:
        logging.error(f"Error in saving object {str(e)}")
        raise CustomException(e,sys)
    
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file:
            obj=pickle.load(file)
        return obj
    except Exception as e:
        logging.error(f"Error in loading object {str(e)}")
        raise CustomException(e,sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for model_name, model in models.items():
            param_grid = params.get(model_name, {})  # Get params safely

            # Apply GridSearchCV only if parameters exist
            if param_grid:
                gs = GridSearchCV(model, param_grid, cv=3)
                gs.fit(X_train, y_train)
                best_params = gs.best_params_
                model.set_params(**best_params)

            # Train model
            model.fit(X_train, y_train)

            # Predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Performance metrics
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score  # Store test score

    except Exception as e:
        raise CustomException(e, sys)

    return report
