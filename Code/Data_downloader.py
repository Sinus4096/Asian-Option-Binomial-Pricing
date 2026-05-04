import yfinance as yf


def download_prices(ticker, start=None, end=None, period="1y", interval="1d", save_path=None):
    try:
        if start or end:
            df = yf.download(tickers=ticker, start=start, end=end, interval=interval, progress=False, auto_adjust=True)
        else:
            df = yf.download(tickers=ticker, period=period, interval=interval, progress=False, auto_adjust=True)
    except Exception as e:
        raise RuntimeError(f"Failed to download data for {ticker}: {e}") from e

    if df.empty:
        raise ValueError(f"No data fetched for {ticker} with the given parameters.")

    if save_path:
        # Prefer "Close", fall back to "Adj Close", otherwise save the last column present
        if "Close" in df.columns:
            to_save = df[["Close"]]
        elif "Adj Close" in df.columns:
            to_save = df[["Adj Close"]]
        else:
            to_save = df.iloc[:, [-1]]
        to_save.to_csv(save_path)

    return df


# Example usage
if __name__ == "__main__":
    df = download_prices("AAPL", start="2019-12-31", end="2026-04-29", interval="1d", save_path="aapl_28apr.csv")
    print(df.tail())





