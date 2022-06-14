from pandas_datareader import data
import pandas as pd

import argparse
from datetime import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="fin-import", description="Retrieves a specific stock's value for a specified period of time.")
    parser.add_argument("symbol", type=str, help="Stock symbol (Ticker)")
    parser.add_argument("-s", "--start", type=str, help="Start date [YYYY-MM-DD] (default: 2010-01-01)")
    parser.add_argument("-e", "--end", type=str, help="End date [YYYY-MM-DD] (default: today)")
    args = parser.parse_args()

    symbol = args.symbol
    start_date = args.start
    end_date = args.end

    panel_data = data.DataReader(symbol, "yahoo", start_date, end_date)

    if start_date == None:
        start_date = "2010-01-01"
    if end_date == None:
        end_date = datetime.today().strftime('%Y-%m-%d')

    f = open(symbol + "_" + start_date + "_" + end_date + ".txt", "w")

    for closeVal in panel_data['Close'].values:
        f.write(str(closeVal) + "\n")

    f.close()
