import csv
import datetime
import json
import os
import requests
import statistics
#import plotly
#import plotly.graph_objs as go
import pandas as pd
import glob



#def to_usd(my_price):
 #   return "${0:,.2f}".format(my_price)

from dotenv import load_dotenv
load_dotenv()

stock_list = ["MSFT", "GOOG", "AAPL"]
weight_list = [.50,.10,.20]

# def merge(stock_list, weight_list): 
#     merged_list = [(stock_list[i], weight_list[i]) for i in range(0, len(stock_list)] 
#     return merged_list 

# while True:
#     stock_symbol = input("Please enter stock symbol or 'DONE' if complete: ")
#     weight = input("Please enter stock weight or 'DONE' if complete example 25 = 25%: ")
#     if stock_symbol == "DONE" and weight =="DONE":
#         break 
#    # elif sum(weight_list) = 100
#      #   break   
#     elif len(stock_symbol) > 5 or weight.isalpha():
#      print("Stock symbol input too long or weight is not formatted correctly, expecting a ticker no more than 5 characters and wieght only contains digits")
#     elif stock_symbol.isalpha() and weight.isdigit():  
#         stock_list.append(stock_symbol)   
#         weight_list.append(weight) 
#     else: 
#         print("Invalid Selection")

#print(stock_list)
#print(weight_list)

#close_prices = []

for symbol in stock_list:
    API_KEY = os.environ.get("ALPHADVANTAGE_API_KEY")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}"
    response = requests.get(request_url)
    response_message = response.text
    parsed_response = json.loads(response.text)
    tsd = parsed_response["Time Series (Daily)"]
    dates = list(tsd.keys())
    for date in dates:
            daily_prices = tsd[date]  
            #close_price = tsd[date]["4. close"]
            #close_prices.append(float((close_price)))
    #print(parsed_response)
    csv_file_path = os.path.join(os.path.dirname(__file__), "data", f"{symbol}.prices.csv")
    #csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
    csv_headers = ["timestamp", "close"]
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices = tsd[date]  
    
    #looping
            writer.writerows.sort({
                "timestamp": date, 
                #"open": daily_prices["1. open"],
                #"high": daily_prices["2. high"],
                #"low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                #"volume": daily_prices["5. volume"]
            })

      
path = r'C:\Users\tyler\Documents\GitHub\Freestyle-Project\data' # use your path
all_files = glob.glob(path + "/*.csv")

li = []
for filename in all_files:
    df = pd.read_csv(filename, header=0).head(5)
    li.append(df)
frame = pd.concat(li, axis=1)
new_frame = frame[['close']]

print(new_frame)

daily_return = new_frame.pct_change(1)
print(new_frame.pct_change(1))
data_frame = daily_return.mul(weight_list)
print(data_frame)

data_frame_sum = data_frame.sum(axis=1)
print(data_frame_sum)

data_sum = data_frame_sum.add(1)
print(data_sum)

data_frame_cum = data_sum.cumprod()
print(data_frame_cum)

#https://stackoverflow.com/questions/40811246/pandas-cumulative-return-function/40811680
# df.ix["Cumulative"] = ((data_frame_sum+1).cumprod()-1).iloc[-1]
# print(df.ix["Cumulative"])



# 