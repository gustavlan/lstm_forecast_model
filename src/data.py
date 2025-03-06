import pandas as pd
import numpy as np
import os

def load_data(filepath: str) -> pd.DataFrame:
    """Load raw data from CSV or Excel."""
    return pd.read_csv(filepath)

def create_lagged_features(df: pd.DataFrame, lag: int = 12) -> pd.DataFrame:
    """Create lagged features for time-series analysis."""
    for i in range(1, lag+1):
        df[f'return_lag_{i}'] = df['return'].shift(i)
    return df.dropna()


