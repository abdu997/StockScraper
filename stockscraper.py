import sys
import csv
import requests 
import json
from datetime import datetime
from pandas.tseries.offsets import BDay

def to_integer(dt_time):
    return str(10000 * dt_time.year + 100 * dt_time.month + dt_time.day)

def GetData(symbol, startdate, days):
    # Get your token from https://iexcloud.io/cloud-login#/register/
    token = ""
    
    data = []

    # Get testing days 
    dates = []
    for x in range(int(days) + 1):
        dates.append(to_integer(datetime.strptime(startdate, '%Y%m%d') + BDay(x)))

    # Fetch backtest period data
    for date in dates:
        url = "https://cloud.iexapis.com/stable/stock/" + symbol + "/chart/date/" + date + "?token=" + token
        for x in requests.get(url = url).json():
            data.append(x)
    return data

symbol = sys.argv[1]
startdate = sys.argv[2]
days = sys.argv[3]
format = sys.argv[4]
filename = sys.argv[5]

data = GetData(symbol, startdate, days)

if format == "csv":
    with open(filename + ".csv", "w") as file:
        csv_file = csv.writer(file)
        keys = []
        for x in data[0]:
            keys.append(x)
        csv_file.writerow(keys)
        for item in data:
            y = []
            for x in keys:
                y.append(item[x])
            csv_file.writerow(y)
elif format == "json":
    with open(filename  + ".json", "w") as file:
        json.dump(data, file)

print ("Done")
