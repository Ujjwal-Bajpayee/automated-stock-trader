import yfinance as yf
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta
import time
from decouple import config 


API_KEY = config('APCA_API_KEY_ID')
API_SECRET = config('APCA_API_SECRET_KEY')
BASE_URL = 'https://paper-api.alpaca.markets'  


api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')


def check_condition(stock_symbol, target_price, start_date, end_date):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    for index, row in stock_data.iterrows():
        if row['Low'] <= target_price <= row['High']:
            return True
    return False


def place_order(stock_symbol, qty, side='buy'):
    try:
        api.submit_order(
            symbol=stock_symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        print(f"Order placed: {side} {qty} shares of {stock_symbol}")

        if side == 'sell':
            print(f"Notification: Sold {qty} shares of {stock_symbol}")
    except Exception as e:
        print(f"An error occurred: {e}")


def monitor_and_trade(stock_symbol, buy_price, sell_price, qty, start_date, end_date):
    bought = False
    while datetime.now() < end_date:
        if not bought and check_condition(stock_symbol, buy_price, start_date, end_date):
            place_order(stock_symbol, qty, side='buy')
            bought = True
        elif bought and check_condition(stock_symbol, sell_price, start_date, end_date):
            place_order(stock_symbol, qty, side='sell')
            return
        time.sleep(60)  


    if bought:
        print(f"Notification: The sell price was not reached for {stock_symbol} within the given time period.")

def get_user_input():
    stock_symbol = input("Enter the stock symbol you want to trade: ").upper()
    buy_price = float(input("Enter the buy price: "))
    sell_price = float(input("Enter the sell price: "))
    qty = int(input("Enter the number of shares to buy: "))
    days = int(input("Enter the number of days to monitor the stock: "))
    return stock_symbol, buy_price, sell_price, qty, days
