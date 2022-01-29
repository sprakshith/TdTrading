import numpy as np


class CalculationUtil:
    def __init__(self, spot, expiry_in_days, implied_volatility):
        self.spot = spot
        self.expiry_in_days = expiry_in_days
        self.implied_volatility = implied_volatility

    def get_flutuation_range(self):
        fluctuation_price = self.spot * (self.implied_volatility/100) * np.sqrt(self.expiry_in_days/365)
        lower_range = round(self.spot - fluctuation_price, 2)
        upper_range = round(self.spot + fluctuation_price, 2)

        return lower_range, upper_range


# model = CalculationUtil(17101.95, 4, 39.60)
# print(model.get_flutuation_range())
