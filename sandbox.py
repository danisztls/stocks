#!/usr/bin/env python

"""
This is a docstring with a description of what this file does.
"""

__author__  = "Daniel Souza <me@posix.dev.br>"
__license__ = "MIT"

import yaml
# https://github.com/yaml/pyyaml

from rich import print
# https://github.com/Textualize/rich

import yfinance
# https://github.com/ranaroussi/yfinance

import pandas
# https://pandas.pydata.org/

# Monitor
def load_portfolio():
    filepath = "portfolio.yml"

    with open(filepath, 'r') as file:
        portfolio = yaml.safe_load(file)
    
    tickers = ""
    for ticker in portfolio:
        tickers += ticker + ' '
    tickers = tickers.strip()

    stocks = yfinance.Tickers(tickers)

    # pandas dataframe
    data = yfinance.download(tickers, period="ytd", group_by="ticker")

    for stock in portfolio:
        print("\n", ":pencil:", f"[blue]{stock}[/blue]")

        # analysts data
        # TODO: Implement a voting algorithm.
        # TODO: For practical reasons translate overweight/underweight to buy/sell
        # TODO: Graph on stdout the grade evolution. 
        recommendation = stocks.tickers[stock].recommendations
        print(recommendation["To Grade"])
        
        # price data
        # print(data[stock])

load_portfolio()

# tickers.tickers.MSFT.info
# tickers.tickers.AAPL.history(period="1mo")
# tickers.tickers.GOOG.actions

# IDEAS
# Goal is to make investing quick and boring as to not waste time and to avoid stress.
# Delegate market analysis to analysts. Don't miss on important events. Monitor performance from the command line. Quickly rebalance portfolio with the use of KPIs and recommendations.

# Monitor
# Show a summary of shares on a portfolio.

# Guardian
# Message important events to Telegram.
# Message reports to Telegram (I can make turn this into a biz).

# Screen
# Screen potential stocks for investment, filter and compare financials side-to-side.

# Libs
# https://github.com/Textualize/rich
# https://github.com/Textualize/textual
# https://github.com/python-telegram-bot/python-telegram-bot

# EXAMPLES

# msft = yf.Ticker("MSFT")

# get stock info
# msft.info

# get historical market data
# hist = msft.history(period="1m")

## show actions (dividends, splits)
# msft.actions

## show dividends
# msft.dividends

## show splits
# msft.splits

## show financials
# msft.financials
# msft.quarterly_financials

## show major holders
# msft.major_holders

## show institutional holders
# msft.institutional_holders

## show balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet

## show cashflow
# msft.cashflow
# msft.quarterly_cashflow

## show earnings
# msft.earnings
# msft.quarterly_earnings

## show sustainability
# msft.sustainability

## show analysts recommendations
# print(msft.recommendations)

## show next event (earnings, etc)
# msft.calendar

## show ISIN code - *experimental*
## ISIN = International Securities Identification Number
# msft.isin

## show options expirations
# msft.options

## show news
# msft.news

## get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
## data available via: opt.calls, opt.puts
