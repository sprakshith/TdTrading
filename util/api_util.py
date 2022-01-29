from backtracker.test_algorithm import TestStockAlgo
import candlepattern.candle_pattern as cp
from util import os_util
from constants import file_path_constants as fpc
import pandas as pd
import json

pattern_dictionary = {
    "Bullish Marubozo": cp.bullish_marubozo_pattern,
    "Bearish Marubozo": cp.bearish_marubozo_pattern,
    "Paper Umbrella": cp.paper_umbrella_pattern,
    "Shooting Star": cp.shooting_star_pattern,
    "Bullish Engulphing": cp.bullish_engulphing_pattern,
    "Bearish Engulphing": cp.bearish_engulphing_pattern,
    "Bullish Harami": cp.bullish_harami_pattern,
    "Bearish Harami": cp.bearish_harami_pattern,
    "Morning Star": cp.morning_star_pattern,
    "Evening Star": cp.evening_star_pattern,
    "Spinning Top": cp.spinning_top_pattern
}


def get_all_tickers():
    data_nifty = pd.read_csv(fpc.NIFTY_50_FILE)
    tickers = [ticker for ticker in data_nifty['Symbol']]

    return json.dumps(tickers)


def get_all_patterns():
    patterns = ['Bullish Marubozo', 'Bearish Marubozo', 'Paper Umbrella', 'Shooting Star', 'Bullish Engulphing',
                'Bearish Engulphing', 'Bullish Harami', 'Bearish Harami', 'Morning Star', 'Evening Star',
                'Spinning Top']

    return json.dumps(patterns)


def get_pattern_occurances():
    df = pd.read_csv(fpc.STOCKS_RESULT_FILE)

    pattern_list = []
    for index in range(len(df)):
        pattern_object = {'Slno': index + 1, 'Date': df.loc[index, 'Date'],
                          'Name': df.loc[index, 'Name'], 'Pattern': df.loc[index, 'Pattern'],
                          'Trend': df.loc[index, 'Trend']}

        pattern_list.append(pattern_object)

    return json.dumps(pattern_list)


def fetch_profit_lost_data(ticker_name, pattern_name):
    stock_ticker = ticker_name + ".NS"

    if ticker_name in ["^NSEI", "^NSEBANK"]:
        stock_ticker = ticker_name

    pattern = pattern_dictionary[pattern_name]
    json_array, df = test_stock_pattern(stock_ticker, pattern)

    return json_array


def test_stock_pattern(stock_ticker, pattern):
    pattern_name = ''.join(pattern.__doc__.split())

    test_algo = TestStockAlgo(stock_ticker, pattern)
    results = test_algo.test_alogorithm()
    list_to_array = json.dumps(results)
    df = pd.DataFrame(results)

    folder_name = stock_ticker.split(".")[0]
    os_util.create_company_directory(folder_name)
    os_util.create_pattern_directory(folder_name, pattern_name)

    filename_json = os_util.get_profit_loss_json_path(folder_name, pattern_name)
    filename_csv = os_util.get_profit_loss_csv_path(folder_name, pattern_name)

    file = open(filename_json, 'w')
    file.write(list_to_array)

    df.to_csv(filename_csv)

    return list_to_array, df
