import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from sktime.datasets import load_airline
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.theta import ThetaForecaster
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error
from sktime.split import temporal_train_test_split
from sktime.utils.plotting import plot_series
import sktime.registry as rfr

def parse_csv(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)

    # Clean data: handle missing values
    data = data.dropna()

    # Convert categorical variables to category dtype
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = data[col].astype('category')

    return data

def get_columns(data):
    return data.columns.tolist()

def example_perform_regression(file_path):
    data = pd.read_csv(file_path)
    cols = get_columns(data)
    df = data[cols]
    return df

def sktime_example():
    # Load the airline dataset
    y = load_airline()

    # Split the data into training and testing sets
    y_train, y_test = temporal_train_test_split(y, test_size=36)

    # Define the forecasting horizon
    fh = ForecastingHorizon(y_test.index, is_relative=False)

    # Initialize and fit the Theta forecaster
    forecaster = ThetaForecaster(sp=12)
    forecaster.fit(y_train)

    # Generate predictions
    y_pred = forecaster.predict(fh)

    # Calculate and return the Mean Absolute Percentage Error (MAPE)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    return plot_series(y)

def time_series_forcasting(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data.index = pd.DatetimeIndex(data.index).to_period('D')
    ts = data['Inventory_Level']

    # Split the data into training and testing sets
    y_train, y_test = temporal_train_test_split(ts, test_size=12)

    # Define the forecasting horizon
    fh = ForecastingHorizon(y_test.index, is_relative=False)

    # Initialize and fit the Theta forecaster
    forecaster = ThetaForecaster(sp=12)
    forecaster.fit(y_train)

    # Generate predictions
    y_pred = forecaster.predict(fh)

    # Calculate and return the Mean Absolute Percentage Error (MAPE)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    return mape

def time_series_forcasting_with_year_filtering(file_path, years=5):
    data = pd.read_csv(file_path, parse_dates=["Date"])
    today = pd.Timestamp.today()
    last_year_df = data[data["Date"] >= (today - pd.DateOffset(years=years))]

    monthly_sum = last_year_df.groupby(last_year_df["Date"].dt.to_period("M"))["Inventory_Level"].sum()
    monthly_sum = monthly_sum.to_timestamp()

    monthly_sum_df = monthly_sum.reset_index()
    monthly_sum_df.columns = ["Month", "Inventory_Sum"]

    ts = monthly_sum_df['Inventory_Sum']
    y_train, y_test = temporal_train_test_split(ts, test_size=12)
    fh = ForecastingHorizon(y_test.index, is_relative=False)
    forecaster = ThetaForecaster(sp=6)
    forecaster.fit(y_train)
    y_pred = forecaster.predict(fh)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    plot_series(y_train, y_pred)
