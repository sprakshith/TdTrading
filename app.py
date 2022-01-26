import time
from api.fetch_stocks_list import fetch_stocks_list
from flask import Flask
from util import api_util

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    return "This website is used as a Rest API.\n"\
           "Created By: <a href=\"https://sprakshith.pythonanywhere.com/aboutUs/\">S P RAKSHITH</a>"


@app.route('/algotrading/refresh_pattern_results/', methods=["POST", "GET"])
def refresh_pattern_results():
    start_time = time.time()
    fetch_stocks_list()
    end_time = time.time()
    return f"Refreshed in {round(end_time - start_time, 2)} seconds."


@app.route('/algotrading/get_pattern_occurances/', methods=["POST", "GET"])
def get_pattern_occurances():
    return api_util.get_pattern_occurances()


@app.route('/algotrading/get_all_tickers/', methods=["POST", "GET"])
def get_all_tickers():
    return api_util.get_all_tickers()


@app.route('/algotrading/get_all_patterns/', methods=["POST", "GET"])
def get_all_patterns():
    return api_util.get_all_patterns()


@app.route('/algotrading/fetch_profit_lost_data/<ticker_name>/<pattern_name>/', methods=["POST", "GET"])
def fetch_profit_lost_data(ticker_name, pattern_name):
    return api_util.fetch_profit_lost_data(ticker_name, pattern_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
