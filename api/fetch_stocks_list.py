import yfinance as yf
from candlepattern import candle_pattern as cp
import pandas as pd
from stockstats import StockDataFrame as Sdf
from constants import candle_stick_constans as csc
from constants import file_path_constants as fpc


def fetch_stocks_list():
    data_nifty = pd.read_csv(fpc.NIFTY_50_FILE)

    scanners = [cp.bullish_marubozo_pattern, cp.bearish_marubozo_pattern,
                cp.paper_umbrella_pattern, cp.shooting_star_pattern,
                cp.bullish_engulphing_pattern, cp.bearish_engulphing_pattern,
                cp.bullish_harami_pattern, cp.bearish_harami_pattern,
                cp.morning_star_pattern, cp.evening_star_pattern]

    pattern = []
    stock_name = []
    date_time = []
    trend = []

    i = 1
    total = len(data_nifty) * len(scanners)
    for ticker in data_nifty['Symbol']:

        ticker_name = ticker + ".NS"

        if ticker in ["^NSEI", "^NSEBANK"]:
            ticker_name = ticker

        data = yf.download(tickers=ticker_name, period="5d")
        stock = Sdf.retype(data)
        stock_refined = stock[['open', 'high', 'low', 'close', 'volume', 'macd', 'macds', 'rsi_14', 'atr']]
        for scanner in scanners:
            try:
                dates = scanner(stock_refined)
                if len(dates) > 0:
                    pattern_name = ''.join(scanner.__doc__.split())

                    is_bullish = pattern_name in csc.BULLISH_CANDLE_STICKS
                    is_bearish = pattern_name in csc.BEARISH_CANDLE_STICKS

                    pattern.append(pattern_name)
                    stock_name.append(ticker)
                    date_time.append(str(max(dates)))

                    if is_bullish:
                        trend.append(csc.BULLISH_TREND)
                    elif is_bearish:
                        trend.append(csc.BEARISH_TREND)
                    else:
                        trend.append(csc.VARYING_TREND)
            except Exception as e:
                print("Error with ", ticker, " ", e)

            print(f"Finished :::::: {i}/{total}.")
            i += 1

    new_dataframe = pd.DataFrame({
        "Pattern": pattern,
        "Name": stock_name,
        "Date": date_time,
        "Trend": trend
    })

    new_dataframe.to_csv(fpc.STOCKS_RESULT_FILE)

    return new_dataframe
