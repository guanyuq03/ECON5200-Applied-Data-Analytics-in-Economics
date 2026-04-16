"""
decompose.py — Time Series Decomposition & Diagnostics Module

Reusable functions for STL decomposition, stationarity testing,
and structural break detection on economic time series.

Author: Guanyu Qu
Course: ECON 5200, Lab 20
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import adfuller, kpss
import ruptures as rpt
from typing import Optional


def run_stl(
    series: pd.Series,
    period: int = 12,
    log_transform: bool = True,
    robust: bool = True
):
    """Apply STL decomposition with optional log-transform.
    
    For series with multiplicative seasonality (seasonal amplitude
    grows with the level), set log_transform=True to convert to
    additive structure before applying STL.
    
    Args:
        series: Time series with DatetimeIndex and set frequency
        period: Seasonal period (12=monthly, 4=quarterly)
        log_transform: Log-transform for multiplicative data
        robust: Downweight outliers via bisquare weights
    
    Returns:
        STL result object
    
    Raises:
        ValueError: if series contains non-positive values with log_transform=True
    """
    if log_transform:
        if (series <= 0).any():
            raise ValueError(
                "Series contains non-positive values. "
                "Cannot log-transform. Set log_transform=False."
            )
        work_series = np.log(series)
    else:
        work_series = series.copy()

    stl = STL(work_series, period=period, robust=robust)
    return stl.fit()


def test_stationarity(
    series: pd.Series,
    alpha: float = 0.05
) -> dict:
    """Run ADF + KPSS and return the 2x2 decision table verdict.
    
    ADF null: unit root (non-stationary)
    KPSS null: stationary
    
    Args:
        series: Time series to test
        alpha: Significance level for both tests
    
    Returns:
        dict with 'adf_stat', 'adf_p', 'kpss_stat', 'kpss_p', 'verdict'
        Verdict is one of: 'stationary', 'non-stationary',
        'contradictory', 'inconclusive'
    """
    # ADF test with constant + trend (safe default for economic data)
    adf_stat, adf_p, _, _, _, _ = adfuller(series, autolag='AIC', regression='ct')

    # KPSS test with constant (trend-stationary alternative)
    kpss_stat, kpss_p, _, _ = kpss(series, regression='ct', nlags='auto')

    adf_rejects = adf_p < alpha
    kpss_rejects = kpss_p < alpha

    if adf_rejects and not kpss_rejects:
        verdict = 'stationary'
    elif not adf_rejects and kpss_rejects:
        verdict = 'non-stationary'
    elif adf_rejects and kpss_rejects:
        verdict = 'contradictory'
    else:
        verdict = 'inconclusive'

    return {
        'adf_stat': adf_stat,
        'adf_p': adf_p,
        'kpss_stat': kpss_stat,
        'kpss_p': kpss_p,
        'verdict': verdict,
    }



def detect_breaks(
    series: pd.Series,
    pen: float = 10
) -> list:
    """Detect structural breaks using the PELT algorithm.
    
    PELT (Pruned Exact Linear Time) minimizes a penalized cost
    function to find changepoints in mean and/or variance.
    
    Args:
        series: Time series with DatetimeIndex
        pen: Penalty parameter (higher = fewer breaks)
    
    Returns:
        List of break dates as pd.Timestamp
    """
    signal = series.values
    algo = rpt.Pelt(model='rbf').fit(signal)
    breakpoints = algo.predict(pen=pen)

    # Convert indices to dates (exclude the final index which is len(series))
    break_dates = [
        series.index[bp - 1]
        for bp in breakpoints
        if bp < len(series)
    ]

    return break_dates
