from __future__ import annotations

import numpy as np
import pandas as pd


def iqr_bounds(series: pd.Series, factor: float = 1.5) -> tuple[float, float]:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return float(q1 - factor * iqr), float(q3 + factor * iqr)


def hampel_filter(series: pd.Series, window: int = 5, n_sigma: float = 3.0) -> pd.Series:
    median = series.rolling(window=window, center=True, min_periods=1).median()
    abs_dev = (series - median).abs()
    mad = abs_dev.rolling(window=window, center=True, min_periods=1).median()
    threshold = 1.4826 * n_sigma * mad
    result = series.copy()
    result[abs_dev > threshold] = median[abs_dev > threshold]
    return result


def robust_zscore(series: pd.Series) -> pd.Series:
    median = series.median()
    mad = np.median(np.abs(series.dropna() - median))
    if mad == 0:
        return pd.Series(0.0, index=series.index)
    return 0.6745 * (series - median) / mad
