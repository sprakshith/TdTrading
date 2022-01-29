import numpy as np


# Code to Get Bullish Marubozo Pattern
def bullish_marubozo_pattern(stocks):
    """
    Bullish Marubozo
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        # Required Dates
        current_date = stocks.index[index]

        try:
            if stocks.loc[current_date, 'close'] > stocks.loc[current_date, 'open']:
                # Candle Values
                current_open = stocks.loc[current_date, 'open']
                current_high = stocks.loc[current_date, 'high']
                current_low = stocks.loc[current_date, 'low']
                current_close = stocks.loc[current_date, 'close']

                # Percentage Changes
                top_change_percentage = get_difference_percentage(current_open, current_high)
                bottom_change_percentage = get_difference_percentage(current_low, current_close)
                open_close_perecentage = get_difference_percentage(current_open, current_close)

                if top_change_percentage <= 0.5 and bottom_change_percentage <= 0.5:
                    if 1 <= open_close_perecentage <= 10:
                        if is_downward_trend(stocks, current_date):
                            dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code to Get Bearish Marubozo Pattern
def bearish_marubozo_pattern(stocks):
    """
    Bearish Marubozo
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        # Required Dates
        current_date = stocks.index[index]

        try:
            if stocks.loc[current_date, 'close'] < stocks.loc[current_date, 'open']:
                # Candle Values
                current_open = stocks.loc[current_date, 'open']
                current_high = stocks.loc[current_date, 'high']
                current_low = stocks.loc[current_date, 'low']
                current_close = stocks.loc[current_date, 'close']

                # Percentage Changes
                top_change_percentage = get_difference_percentage(current_open, current_high)
                bottom_change_percentage = get_difference_percentage(current_low, current_close)
                open_close_perecentage = get_difference_percentage(current_open, current_close)

                if top_change_percentage <= 0.5 and bottom_change_percentage <= 0.5:
                    if 1 <= open_close_perecentage <= 10:
                        if is_upward_trend(stocks, current_date):
                            dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code to Get Paper Umbrella Pattern
def paper_umbrella_pattern(stocks):
    """
    Paper Umbrella
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        # Required Dates
        current_date = stocks.index[index]

        # Candle Values
        current_open = stocks.loc[current_date, 'open']
        current_high = stocks.loc[current_date, 'high']
        current_low = stocks.loc[current_date, 'low']
        current_close = stocks.loc[current_date, 'close']

        # Percentage Change
        difference_open_high = get_difference_percentage(current_open, current_high)
        difference_close_high = get_difference_percentage(current_close, current_high)
        difference_open_low = get_difference_percentage(current_low, current_open)
        difference_close_low = get_difference_percentage(current_low, current_close)

        try:
            if current_open > current_close and difference_open_high <= 0.25:
                difference_open_close = get_difference_percentage(current_close, current_open)
                if difference_close_low >= (difference_open_close * 2):
                    dates_list.append(current_date)
            elif current_close > current_open and difference_close_high <= 0.25:
                difference_open_close = get_difference_percentage(current_open, current_close)
                if difference_open_low >= (difference_open_close * 2):
                    dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code to Get Shooting Start Pattern
def shooting_star_pattern(stocks):
    """
    Shooting Star
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        # Required Dates
        current_date = stocks.index[index]

        # Candle Values
        current_open = stocks.loc[current_date, 'open']
        current_high = stocks.loc[current_date, 'high']
        current_low = stocks.loc[current_date, 'low']
        current_close = stocks.loc[current_date, 'close']

        # Percentage Change
        difference_high_open = get_difference_percentage(current_high, current_open)
        difference_high_close = get_difference_percentage(current_high, current_close)
        difference_open_low = get_difference_percentage(current_open, current_low)
        difference_close_low = get_difference_percentage(current_close, current_low)

        try:
            if current_open > current_close and difference_close_low <= 0.25:
                difference_open_close = get_difference_percentage(current_open, current_close)
                if difference_high_open >= (difference_open_close * 2):
                    dates_list.append(current_date)
            elif current_close > current_open and difference_open_low <= 0.25:
                difference_close_open = get_difference_percentage(current_close, current_open)
                if difference_high_close >= (difference_close_open * 2):
                    dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code to Get Bullish Engulphing Pattern
def bullish_engulphing_pattern(stocks):
    """
    Bullish Engulphing
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        previous_date = stocks.index[index - 1]
        current_date = stocks.index[index]

        # Candle Values - Previous Date
        previous_open = stocks.loc[previous_date, 'open']
        previous_close = stocks.loc[previous_date, 'close']

        # Candle Values - Current Date
        current_open = stocks.loc[current_date, 'open']
        current_close = stocks.loc[current_date, 'close']

        try:
            if current_close > current_open:
                if previous_close < previous_open:
                    if (previous_close > current_open) and (previous_open < current_close):
                        if is_downward_trend(stocks, current_date):
                            dates_list.append(current_date)
                if previous_open < previous_close:
                    if (previous_close > current_close) and (previous_open < current_open):
                        if is_downward_trend(stocks, current_date):
                            dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code to Get Bearish Engulphing Pattern
def bearish_engulphing_pattern(stocks):
    """
    Bearish Engulphing
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        previous_date = stocks.index[index - 1]
        current_date = stocks.index[index]

        # Candle Values - Previous Date
        previous_open = stocks.loc[previous_date, 'open']
        previous_close = stocks.loc[previous_date, 'close']

        # Candle Values - Current Date
        current_open = stocks.loc[current_date, 'open']
        current_close = stocks.loc[current_date, 'close']

        try:
            if current_open > current_close:
                if previous_close < previous_open:
                    if (previous_close > current_close) and (previous_open < current_open):
                        if is_upward_trend(stocks, current_date):
                            dates_list.append(current_date)
                if previous_open < previous_close:
                    if (previous_open > current_close) and (previous_close < current_open):
                        if is_upward_trend(stocks, current_date):
                            dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code for the Bullish Harami Pattern
def bullish_harami_pattern(stocks):
    """
    Bullish Harami
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        previous_date = stocks.index[index - 1]
        current_date = stocks.index[index]

        # Candle Values - Previous Date
        previous_open = stocks.loc[previous_date, 'open']
        previous_close = stocks.loc[previous_date, 'close']

        # Candle Values - Current Date
        current_open = stocks.loc[current_date, 'open']
        current_close = stocks.loc[current_date, 'close']

        try:
            if (previous_close < previous_open) and (current_close > current_open):
                if (previous_close < current_open) and (previous_open > current_close):
                    if is_downward_trend(stocks, current_date):
                        dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code for the Bearish Harami Pattern
def bearish_harami_pattern(stocks):
    """
    Bearish Harami
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        previous_date = stocks.index[index - 1]
        current_date = stocks.index[index]

        # Candle Values - Previous Date
        previous_open = stocks.loc[previous_date, 'open']
        previous_close = stocks.loc[previous_date, 'close']

        # Candle Values - Current Date
        current_open = stocks.loc[current_date, 'open']
        current_close = stocks.loc[current_date, 'close']

        try:
            if (previous_close > previous_open) and (current_close < current_open):
                if (previous_close > current_open) and (previous_open < current_close):
                    if is_upward_trend(stocks, current_date):
                        dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code for Morning Star
def morning_star_pattern(stocks):
    """
    Morning Star
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        previous_date_1 = stocks.index[index - 2]
        previous_date_0 = stocks.index[index - 1]
        current_date = stocks.index[index]

        # Candle Values Two Days Before Current Day
        previous_1_open = stocks.loc[previous_date_1, 'open']
        previous_1_close = stocks.loc[previous_date_1, 'close']

        # Candle Values - Previous Date
        previous_open = stocks.loc[previous_date_0, 'open']
        previous_close = stocks.loc[previous_date_0, 'close']

        # Candle Values - Current Date
        current_open = stocks.loc[current_date, 'open']
        current_close = stocks.loc[current_date, 'close']

        try:
            if previous_1_open > previous_1_close:
                if (previous_open < previous_1_close) and (previous_close < previous_1_close):
                    if (current_open > previous_open) and (current_open > previous_close):
                        if current_close > current_open:
                            if is_downward_trend(stocks, current_date):
                                dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code for Evening Star
def evening_star_pattern(stocks):
    """
    Evening Star
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        previous_date_1 = stocks.index[index - 2]
        previous_date_0 = stocks.index[index - 1]
        current_date = stocks.index[index]

        # Candle Values Two Days Before Current Day
        previous_1_open = stocks.loc[previous_date_1, 'open']
        previous_1_close = stocks.loc[previous_date_1, 'close']

        # Candle Values - Previous Date
        previous_open = stocks.loc[previous_date_0, 'open']
        previous_close = stocks.loc[previous_date_0, 'close']

        # Candle Values - Current Date
        current_open = stocks.loc[current_date, 'open']
        current_close = stocks.loc[current_date, 'close']

        try:
            if previous_1_open < previous_1_close:
                if (previous_open > previous_1_close) and (previous_close > previous_1_close):
                    if (current_open < previous_open) and (current_open < previous_close):
                        if current_close < current_open:
                            if is_upward_trend(stocks, current_date):
                                dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


# Code to get Spinning Top Pattern
def spinning_top_pattern(stocks):
    """
    Spinning Top
    """
    dates_list = []
    for index in range(1, len(stocks.index)):
        # Required Dates
        current_date = stocks.index[index]

        # Candle Values
        current_open = stocks.loc[current_date, 'open']
        current_high = stocks.loc[current_date, 'high']
        current_low = stocks.loc[current_date, 'low']
        current_close = stocks.loc[current_date, 'close']

        try:
            if get_difference_percentage(current_open, current_high) <= 1:
                if current_open > current_close:
                    difference_close_low = get_difference_percentage(current_low, current_close)
                    differenc_open_high = get_difference_percentage(current_open, current_high)
                    if difference_close_low <= 1 and differenc_open_high <= 1:
                        dates_list.append(current_date)
                else:
                    difference_close_high = get_difference_percentage(current_close, current_high)
                    differenc_open_low = get_difference_percentage(current_low, current_open)
                    if difference_close_high <= 1 and differenc_open_low <= 1:
                        dates_list.append(current_date)
        except Exception as e:
            print(e)

    return dates_list


def is_downward_trend(stocks, occurance_date):
    return get_close_difference_mean(stocks, occurance_date) > 0


def is_upward_trend(stocks, occurance_date):
    return get_close_difference_mean(stocks, occurance_date) < 0


def get_close_difference_mean(stocks, occurance_date):
    filtered_dates = stocks.loc[:occurance_date].index[-5:]

    difference_list = []
    for i in range(len(filtered_dates)):
        if i > 0:
            current_date = filtered_dates[i]
            previous_date = filtered_dates[i - 1]
            difference_list.append(stocks.loc[previous_date, 'close'] - stocks.loc[current_date, 'close'])

    return np.mean(difference_list)


def get_difference_percentage(value_a, value_b):
    difference = value_b - value_a
    return abs((difference / value_a) * 100)
