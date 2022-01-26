import yfinance as yf
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
        return sb.create_profit_loss_table(self.dates, self.stock_refined, list_of_days)
