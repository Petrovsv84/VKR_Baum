import pickle
import numpy as np
import pandas as pd


def load_rast(path='models/Catboost_rast.pkl'):
    with open(path, 'rb') as f:
        cat_rast = pickle.load(f)
    return cat_rast


def load_upr(path='models/Catboost_upr.pkl'):
    with open(path, 'rb') as f:
        cat_upr = pickle.load(f)
    return cat_upr


def load_scaler(path='models/Catboost_scaler.pkl'):
    with open(path, 'rb') as f:
        scaler = pickle.load(f)
    return scaler


def predictUPR(X_ML, model):
    y_upr_pred = cat_upr.predict(X_ML)
    return y_upr_pred


def predictRAST(X_ML, model):
    y_rast_pred = cat_rast.predict(X_ML)
    return y_rast_pred
