import numpy as np


def get_logarithmic_percentage(value_a, value_b):
    return round(np.log(value_b / value_a) * 100, 2)


def get_standard_deviationg(values):
    return round(np.std(values), 2)


def get_average_deviationg(values):
    return round(np.mean(values), 2)


def get_average_and_volatility(data):
    diff_list = []
    for i in data.index:
        if i != 0:
            diff_list.append(get_logarithmic_percentage(data.loc[i - 1, "close"], data.loc[i, "close"]))
        else:
            diff_list.append(np.nan)

    data['Diff'] = diff_list

    mean = get_average_deviationg(data['Diff'].dropna())
    daily_volatility = get_standard_deviationg(data['Diff'].dropna())

    return mean, daily_volatility


class CalculationUtil:
    def __init__(self, data, spot, expiry_in_days, daily_average=None, daily_volatility=None):
        self.data = data
        self.spot = spot
        self.expiry_in_days = expiry_in_days

        daile_value_tuple = get_average_and_volatility(data)

        if daily_average is None:
            self.daily_average = daile_value_tuple[0]
        else:
            self.daily_average = daily_average

        if daily_volatility is None:
            self.daily_volatility = daile_value_tuple[1]
        else:
            self.daily_volatility = daily_volatility

    def get_flutuation_range(self):
        new_average = self.daily_average * self.expiry_in_days
        new_volatility = self.daily_volatility * np.sqrt(self.expiry_in_days)

        upper_range_percentage = new_average + new_volatility
        lower_range_percentage = new_average - new_volatility

        upper_range = round(self.spot * np.exp(upper_range_percentage / 100), 2)
        lower_range = round(self.spot * np.exp(lower_range_percentage / 100), 2)

        return upper_range, lower_range
