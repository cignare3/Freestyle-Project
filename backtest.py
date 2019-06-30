import csv
import datetime
import json
import os
import requests
import statistics
#import plotly
#import plotly.graph_objs as go

#def to_usd(my_price):
 #   return "${0:,.2f}".format(my_price)

from dotenv import load_dotenv
load_dotenv()

stock_list = []
weight_list = []

while True:
    stock_symbol = input("Please enter stock symbol or 'DONE' if complete: ")
    weight = input("Please enter stock weight or 'DONE' if complete example 25 = 25%: ")
    if stock_symbol == "DONE" and weight =="DONE":
        break 
   # elif sum(weight_list) = 100
     #   break   
    elif len(stock_symbol) > 5 or weight.isalpha():
     print("Stock symbol input too long or weight is not formatted correctly, expecting a ticker no more than 5 characters and wieght only contains digits")
    elif stock_symbol.isalpha() and weight.isdigit():  
        stock_list.append(stock_symbol)   
        weight_list.append(weight) 
    else: 
        print("Invalid Selection")

print(stock_list)
print(weight_list)

for symbol in stock_list:
    API_KEY = os.environ.get("ALPHADVANTAGE_API_KEY")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    response_message = response.text
    parsed_response = json.loads(response.text)
    tsd = parsed_response["Time Series (Daily)"]
    dates = list(tsd.keys())
    #print(parsed_response)
    csv_file_path = os.path.join(os.path.dirname(__file__), "data", f"{symbol}.prices.csv")
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices = tsd[date]    
    #looping
            writer.writerow({
                "timestamp": date, 
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"],
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                "volume": daily_prices["5. volume"]
            })

#last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#tsd = parsed_response["Time Series (Daily)"]
#dates = list(tsd.keys())