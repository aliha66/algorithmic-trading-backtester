import yfinance as yf

def load_data(ticker):
    """Download 5 years of daily data for a ticker and return the DataFrame."""
    data = yf.download(
        ticker,
        period="5y",
        interval="1d",
        auto_adjust=True,
    )
    return data


if __name__ == "__main__":
    data = load_data("AAPL")
    print(data.head())
    print(data.info())