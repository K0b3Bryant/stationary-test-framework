# Stationarity Testing Framework

## Overview
This framework provides tools for testing the stationarity of time series data using statistical methods like the Augmented Dickey-Fuller (ADF) test and the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test. It supports rolling window analysis and generates detailed outputs for multiple series.

---

## Key Features
1. **Stationarity Tests**:
   - **ADF Test**: Tests the null hypothesis that a unit root is present (non-stationary series).
   - **KPSS Test**: Tests the null hypothesis that the series is stationary.

2. **Rolling Window Analysis**:
   - Performs rolling stationarity tests to analyze stationarity over time.

3. **Multi-Series Support**:
   - Handles multiple time series in a single DataFrame and outputs results for each series individually.

4. **Configurable Parameters**:
   - Parameters like date format, significance levels, and rolling window size can be adjusted in the configuration file.

---

## Project Structure
- **main.py**: Entry point for the framework. Runs stationarity tests and outputs results.
- **utils.py**: Core functions for input validation, stationarity tests, and rolling analysis.
- **config.py**: Centralized configuration for test parameters.

---

## Usage
1. Prepare your input data as a DataFrame with the following columns:
   - `Date`: The date for each observation (YYYY-MM-DD format).
   - One or more columns representing time series values (e.g., `Series1`, `Series2`).

2. Update the `CONFIG` file as needed:
   - `date_format`: Format of the date column (default is `%Y-%m-%d`).
   - `p_value_threshold`: Threshold for determining significance (default is `0.05`).
   - `rolling_window_size`: Window size for rolling analysis (default is `20`).

3. Run `main.py` to execute stationarity tests and view the results:
   - Outputs stationarity test results for all series.
   - Includes rolling stationarity results if enabled.

---
