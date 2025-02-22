# Stock Trading Bot

A Python-based stock trading bot that monitors stock prices and executes buy/sell orders based on user-defined conditions. It uses the Alpaca API for trading and `yfinance` for fetching stock data.

## Features

- **User Input**: Asks the user for the stock symbol, buy price, sell price, quantity, and monitoring period.
- **Automated Trading**: Places buy and sell orders automatically when conditions are met.
- **Sell Notification**: Notifies the user when a sell order is executed.
- **Time Limit Handling**: Alerts the user if the sell price is not reached within the specified time period.

## Prerequisites

1. **Alpaca Account**: Sign up at [Alpaca](https://alpaca.markets/) and get your API key and secret.
2. **Python 3.8+**: Ensure Python is installed on your system.

