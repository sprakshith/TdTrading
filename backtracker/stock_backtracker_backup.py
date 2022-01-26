import pandas as pd


def get_result_for_current_iteration(date, profit, stoploss, stocks):
    date_index = list(stocks.index).index(date)

    # Percentage Change
    percentage_change_high = 0
    percentage_change_low = 0

    # Pattern Data Close Value
    patten_day_close = stocks.loc[date, 'close']

    iteration = 0
    while percentage_change_high < profit and percentage_change_low > -stoploss:
        if (date_index + iteration) < len(stocks):
            current_date = stocks.index[date_index + iteration]

            current_high = stocks.loc[current_date, 'high']
            current_low = stocks.loc[current_date, 'low']

            percentage_change_high = get_percentage_differece(patten_day_close, current_high)
            percentage_change_low = get_percentage_differece(patten_day_close, current_low)
        else:
            break

        iteration += 1

    if percentage_change_high >= profit:
        return 1, stocks.loc[date, 'rsi_14'], stocks.loc[date, 'macd'], stocks.loc[date, 'macds']
    elif percentage_change_low <= -stoploss:
        return 0, stocks.loc[date, 'rsi_14'], stocks.loc[date, 'macd'], stocks.loc[date, 'macds']

    return 2, stocks.loc[date, 'rsi_14'], stocks.loc[date, 'macd'], stocks.loc[date, 'macds']


def backtrack_stock(dates, profit, stoploss, stocks):

    # DataFrame
    result = []
    macd = []
    macds = []
    rsi = []

    for date in dates:
        fetched_results = get_result_for_current_iteration(date, profit, stoploss, stocks)
        result.append(fetched_results[0])
        rsi.append(fetched_results[1])
        macd.append(fetched_results[2])
        macds.append(fetched_results[3])

    df = pd.DataFrame({
        'DATE': dates,
        'RESULT': result,
        'RSI': rsi,
        'MACD': macd,
        'MACDS': macds
    })

    return df


def get_percentage_differece(value_a, value_b):
    difference = value_b - value_a
    return (difference / value_a) * 100
