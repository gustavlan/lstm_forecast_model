import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm

def create_quantile_portfolios(predictions: pd.Series, n_quantiles: int = 5) -> dict:
    """Sort predictions into quantile portfolios."""
    quantiles = pd.qcut(predictions, q=n_quantiles, labels=False)
    portfolios = {i: predictions[quantiles == i] for i in range(n_quantiles)}
    return portfolios

def run_factor_regression(portfolio_returns: pd.Series, factors: pd.DataFrame) -> OLS:
    """Run regression of portfolio returns on factor returns."""
    factors = sm.add_constant(factors)
    model = sm.OLS(portfolio_returns, factors).fit(cov_type='HAC', cov_kwds={'maxlags': 12})
    return model
