"""
forecast_evaluation.py — Forecast Evaluation & Backtesting Module

Reusable functions for computing MASE and running expanding-window
backtests on time series forecasting models.

Author: Guanyu Qu
Course: ECON 5200, Lab 21
"""

import numpy as np
import pandas as pd
from typing import Callable
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.model_selection import TimeSeriesSplit


def compute_mase(actual: np.ndarray, predicted: np.ndarray, 
                 train: np.ndarray, m: int = 12) -> float:
    """Compute Mean Absolute Scaled Error.
    
    Args:
        actual: Array of actual out-of-sample values.
        predicted: Array of predicted values (same length as actual).
        train: Array of in-sample training values.
        m: Seasonal period for naive benchmark (12 for monthly).
    
    Returns:
        MASE value. < 1 means model beats seasonal naive.
    """
    # YOUR IMPLEMENTATION HERE
    # Hint:
    # mae_forecast = np.mean(np.abs(actual - forecast))
    # naive_errors = insample[m:] - insample[:-m]
    # mae_naive = np.mean(np.abs(naive_errors))
    # return mae_forecast / mae_naive
    forecast_mae = np.abs(actual - predicted).mean()
    naive_mae = np.abs(train[m:] - train[:-m]).mean()
    return forecast_mae / naive_mae


def backtest_expanding_window(series: pd.Series, model_fn, 
                               n_splits: int = 5) -> list:
    """Expanding-window backtest for time series models.
    
    Args:
        series: Full time series (pandas Series with DatetimeIndex).
        model_fn: Callable that takes (train_series) and returns 
                  predicted values for h steps ahead.
        n_splits: Number of expanding windows.
    
    Returns:
        List of MASE scores, one per split.
    """
    # YOUR IMPLEMENTATION HERE
    # Hint: loop from min_train to len(series)-horizon, stepping by step
    # For each origin:
    #   train = series[:origin]
    #   actual = series[origin:origin+horizon].values
    #   forecast = model_fn(train)
    #   compute errors and MASE
    
    tscv = TimeSeriesSplit(n_splits=n_splits)
    mase_scores = []
    
    for train_idx, test_idx in tscv.split(series):
        train = series.iloc[train_idx]
        test = series.iloc[test_idx]
        h = len(test)
        
        predicted = model_fn(train, h)
        mase = compute_mase(test.values, predicted, train.values, m=12)
        mase_scores.append(mase)
    
    return mase_scores
