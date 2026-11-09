import pandas as pd
from data_loader import load_data

data_frame = load_data("AAPL")
closing_prices = data_frame["Close", "AAPL"]


def SMA(closing_prices, window_size):
    """
    SMA: simple moving avg of closing prices

    SMA_t = (P_t + P_t-1 + ... + P_t-n+1) / n
        where P is the closing price , 
        t is the current trading day, and
        n is the number of trading days in the window
    Param:
        closing_prices: pd.Series
            Closing prices, indexed by date
        window_size: int
            number of trading days in each window n
    Return:
        pd.Series
            same length and index as closing_prices
            the first window_size -1 values are NaN
    """
    if not isinstance(window_size, int) or window_size < 1:
        raise ValueError("Window size must be positive integer")
    
    return closing_prices.rolling(window = window_size).mean()

if __name__ == "__main__":
    data_frame = load_data("AAPL")
    closing_prices = data_frame["Close", "AAPL"]

    sma_20 = SMA(closing_prices, 20)

    print(type(closing_prices))
    print(sma_20.tail())
