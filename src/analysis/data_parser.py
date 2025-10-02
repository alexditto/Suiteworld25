import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

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

def perform_regression(data, formula):
    # Fit a linear regression model using statsmodels
    model = smf.ols(formula=formula, data=data).fit()
    return model

