#!/usr/bin/env python

"""
Convert a CSV broker statement for import with a portfolio manager.
"""

__author__  = "Daniel Souza <me@posix.dev.br>"
__license__ = "GPLv3"

import argparse
import pandas

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',  dest='input',  help="Input CSV")
parser.add_argument('-o', '--output', dest='output', help="Output CSV")
args = parser.parse_args()

# TODO: It's hardcoded. Abstract flow and config.
"""Read, parse and write CSV to disk"""
def parse(input, output):
    # read from disk
    config = {
        "encoding": 'unicode_escape',
        "engine": 'python',
        "infer_datetime_format": True,
        "sep": ';',
        "skiprows": 0,
        "header": 1,
        "usecols": [0, 2, 3, 4, 5, 6, 7],
        "parse_dates": [0]
    }
    
    raw = pandas.read_csv(input, **config)

    # parse data
    data = pandas.DataFrame()
    data[["Ticker", "Date", "Price"]] = raw[["Ativo", "Dt. Negociação", "Preço"]]
    data["Shares"] = raw["Quantidade Compra"] - raw["Quantidade Venda"]
    data["Type"] = data["Shares"].apply(lambda x: "BUY" if x > 0 else "SELL")

    # save to disk
    data.to_csv(output)

def main():
    parse(args.input, args.output)

main()
