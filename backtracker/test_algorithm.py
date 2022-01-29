import yfinance as yf
from constants import  candle_stick_constans as csc
from backtracker import stock_backtracker as sb
from stockstats import StockDataFrame as Sdf


class TestStockAlgo:
    def __init__(self, ticker, scanner):
        self.ticker = ticker
        self.scanner = scanner
        self.data = yf.download(tickers=ticker, period="max")
        self.stock = Sdf.retype(self.data)
        self.stock_refined = self.stock[['open', 'high', 'low', 'close', 'volume', 'macd', 'macds', 'rsi_14', 'atr']]
        self.dates = scanner(self.stock_refined)

    def test_alogorithm(self, list_of_days=None):
        results = sb.create_profit_loss_table(self.dates, self.stock_refined, list_of_days)

        pattern_name = ''.join(self.scanner.__doc__.split()).replace(" ", "")

        is_bullish = pattern_name in csc.BULLISH_CANDLE_STICKS
        is_bearish = pattern_name in csc.BEARISH_CANDLE_STICKS

        for obj in results:
            p_and_l = obj['P&L']

            if is_bullish:
                if p_and_l > 0:
                    obj['Trend'] = csc.BULLISH_TREND
                else:
                    obj['Trend'] = csc.BEARISH_TREND
            elif is_bearish:
                if p_and_l < 0:
                    obj['Trend'] = csc.BULLISH_TREND
                else:
                    obj['Trend'] = csc.BEARISH_TREND
            else:
                obj['Trend'] = csc.VARYING_TREND

        return results

    def update_profit_loss_color(self, df):
        pattern_name = ''.join(self.scanner.__doc__.split()).replace(" ", "")

        is_bullish = pattern_name in csc.BULLISH_CANDLE_STICKS
        is_bearish = pattern_name in csc.BEARISH_CANDLE_STICKS

        for index in range(len(df)):
            p_and_l = df.loc[index, 'P&L']

            if is_bullish:
                if p_and_l > 0:
                    df.loc[index, 'Trend'] = csc.BULLISH_TREND
                else:
                    df.loc[index, 'Trend'] = csc.BEARISH_TREND
            elif is_bearish:
                if p_and_l < 0:
                    df.loc[index, 'Trend'] = csc.BULLISH_TREND
                else:
                    df.loc[index, 'Trend'] = csc.BEARISH_TREND
            else:
                df.loc[index, 'Trend'] = csc.VARYING_TREND

        return df

