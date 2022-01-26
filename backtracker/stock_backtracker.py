from util.date_util import timestamp_to_string


def get_percentage_differece(value_a, value_b):
    difference = value_b - value_a
    return (difference / value_a) * 100


def get_profit_loss_count(occurance_date, stocks, days):
    required_dates = stocks.loc[occurance_date:].index[:days+1]
    last_date = required_dates[-1]

    occurance_date_close = stocks.loc[occurance_date, 'close']
    last_date_close = stocks.loc[last_date, 'close']

    return get_percentage_differece(occurance_date_close, last_date_close)


def create_profit_loss_table(occurance_dates, stocks, list_of_days=None):
    if list_of_days is None:
        list_of_days = [5, 10, 15, 20]

    result_list = []
    for occurance_date in occurance_dates:
        for days in list_of_days:
            data_table = dict()
            data_table["DATE"] = timestamp_to_string(occurance_date)
            data_table["DAYS"] = days
            data_table["P&L"] = round(get_profit_loss_count(occurance_date, stocks, days), 2)
            data_table["VOLUME"] = float(stocks.loc[occurance_date, 'volume'])
            data_table["MACD"] = round(float(stocks.loc[occurance_date, 'macd']), 4)
            data_table["MACDS"] = round(float(stocks.loc[occurance_date, 'macds']), 4)
            data_table["RSI14"] = round(float(stocks.loc[occurance_date, 'rsi_14']), 2)
            result_list.append(data_table)

    return result_list
