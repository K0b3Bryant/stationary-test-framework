import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from config import CONFIG

def validate_inputs(returns_data: pd.DataFrame):
    # Ensure required columns exist
    if 'Date' not in returns_data.columns or 'Returns' not in returns_data.columns:
        raise ValueError("Returns data must have 'Date' and 'Returns' columns.")

    # Check date formats and ensure consistency
    returns_data['Date'] = pd.to_datetime(returns_data['Date'], format=CONFIG['date_format'])

    # Check for missing values
    if returns_data.isnull().values.any():
        raise ValueError("Returns data contains missing values.")

    # Validate return values (optional log return validation)
    if CONFIG['return_type'] == 'log':
        if not np.allclose(returns_data['Returns'], np.log1p(returns_data['Returns']), atol=0.05):
            raise ValueError("Log returns are inconsistent with a 5% tolerance.")

    return returns_data

def test_stationarity(data: pd.DataFrame):
    returns = data['Returns']
    result = adfuller(returns)
    output = {
        'Test Statistic': result[0],
        'p-value': result[1],
        'Lags Used': result[2],
        'Number of Observations': result[3],
        'Critical Values': result[4]
    }

    # Add stationarity interpretation
    output['Stationary'] = result[1] < CONFIG['p_value_threshold']
    return output
