import yfinance as yf
from candlepattern import candle_pattern as cp
import pandas as pd
from stockstats import StockDataFrame as Sdf


def fetch_stocks_list():
    data_nifty = pd.read_csv('../Data/nifty/nifty_50.csv')

    scanners = [cp.bullish_marubozo_pattern, cp.bearish_marubozo_pattern, cp.paper_umbrella_pattern,
                cp.shooting_star_pattern, cp.bullish_engulphing_pattern, cp.bearish_engulphing_pattern,
                cp.bullish_harami_pattern, cp.bearish_harami_pattern, cp.morning_star_pattern,
                cp.evening_star_pattern, cp.spinning_top_pattern]

    pattern = []
    stock_name = []
    date_time = []

    i = 1
    total = len(data_nifty) * len(scanners)
    for ticker in data_nifty['Symbol']:

        ticker_name = ticker + ".NS"

        if ticker in ["^NSEI", "^NSEBANK"]:
            ticker_name = ticker

        data = yf.download(tickers=ticker_name, period="1mo")
        stock = Sdf.retype(data)
        stock_refined = stock[['open', 'high', 'low', 'close', 'volume', 'macd', 'macds', 'rsi_14', 'atr']]
        for scanner in scanners:
            try:
                dates = scanner(stock_refined)
                if len(dates) > 0:
                    pattern.append(''.join(scanner.__doc__.split()))
                    stock_name.append(ticker)
                    date_time.append(str(max(dates)))
            except Exception as e:
                print("Error with ", ticker, " ", e)

            print(f"Finished :::::: {i}/{total}.")
            i += 1

    new_dataframe = pd.DataFrame({
        "Pattern": pattern,
        "Name": stock_name,
        "Date": date_time
    })

    new_dataframe.to_csv("../Data/result/stocks_results.csv")

    return new_dataframe
