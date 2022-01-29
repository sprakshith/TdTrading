# import numpy as np


# def get_logarithmic_percentage(value_a, value_b):
#     return round(np.log(value_b / value_a) * 100, 2)
#
#
# def get_standard_deviationg(values):
#     return round(np.std(values), 2)
#
#
# def get_average_deviationg(values):
#     return round(np.mean(values), 2)
#
#
# def get_average_and_volatility(data):
#     diff_list = []
#     for i in range(len(data.index)):
#         previous_date = data.index[i - 1]
#         current_date = data.index[i]
#
#         if i != 0:
#             diff_list.append(get_logarithmic_percentage(data.loc[previous_date, "Close"], data.loc[current_date, "Close"]))
#         else:
#             diff_list.append(np.nan)
#
#     data['Diff'] = diff_list
#
#     mean = get_average_deviationg(data['Diff'].dropna())
#     daily_volatility = get_standard_deviationg(data['Diff'].dropna())
#
#     print("Mean: ", mean)
#     print("daily_volatility: ", daily_volatility)
#
#     return mean, daily_volatility
