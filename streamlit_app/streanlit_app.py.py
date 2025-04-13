import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
import joblib
import os
from datetime import datetime, time
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import load_model

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_file = os.path.join(base_dir, 'data', 'sp500    _data.csv')
sp500_stocks=pd.read_csv(csv_file_path)

def calculate_moving_averages(data, window_size):
    return data.rolling(window=window_size).mean()



