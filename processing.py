import pickle
import scikit-learn
import pandas as pd
import numpy as np


def load_matr(path='models/Neuro/'):
    model = tf.keras.models.load_model(path)
    return model


def load_scaler(path='models/Scaler_neur.pkl'):
    with open(path, 'rb') as f:
        scaler = pickle.load(f)
    return scaler
