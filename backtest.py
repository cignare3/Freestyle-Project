import csv
import datetime
import json
import os
import requests
import statistics
import plotly
import plotly.graph_objs as go
import pandas as pd
import glob
import math

def to_usd(my_price):
    return "{0:,.2f}".format(my_price)
def percent(my_price):
    return "{0:.2%}".format(my_price)

from dotenv import load_dotenv
load_dotenv()

#Delete old CSV files from path:

path = r'C:\Users\tyler\Documents\GitHub\Freestyle-Project\data' # use your path
old_files = glob.glob(path + "/*.csv")
for f in old_files:
        os.remove(f)


# stock_list = ["MSFT", "GOOG", "AAPL"]
# weight_list = [.50,.10,.20]

stock_list = []
weight_list = []

while True:
    stock_symbol = input("Please enter stock symbol or 'DONE' if complete: ")
    weight = float(input("Please enter stock weight or '0' if complete example .25 = 25%: "))
    if stock_symbol == "DONE" and weight == 0:
        break 
   # elif sum(weight_list) = 100
     #   break   
    elif len(stock_symbol) > 5 or weight > 1 or weight < 0:
     print("Stock symbol input too long or weight is not formatted correctly, expecting a ticker no more than 5 characters and weight only contains digits")
    elif stock_symbol.isalpha(): #and weight.isdigit():  
        stock_list.append(stock_symbol)   
        weight_list.append(weight) 
    else: 
        print("Invalid Selection")


#Specify Number of Days going back to be tested:
while True:
    Days_tested = input("Please enter number of trading days to be tested: ")
    if Days_tested.isalpha():
        print("Invalid input, please input number")
    else: 
        break

#Convert Days Input to a Intiger 
days = int(Days_tested)

#print(stock_list)
# print(weight_list)
# print(type(weight_list))

for symbol in stock_list:
    API_KEY = os.environ.get("ALPHADVANTAGE_API_KEY")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}"
    response = requests.get(request_url)
    response_message = response.text


#If Data Call Returns and Error:
    if "Error" in response_message:
        print("Invalid Stock Symbol please try again")
        quit()


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
            writer.writerow({
                "timestamp": date, 
                #"open": daily_prices["1. open"],
                #"high": daily_prices["2. high"],
                #"low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                #"volume": daily_prices["5. volume"]
            })

#Read CSV files into Pandas Data Frame
path = r'C:\Users\tyler\Documents\GitHub\Freestyle-Project\data' # use your path
all_files = glob.glob(path + "/*.csv")

li = []
for filename in all_files:
    df = pd.read_csv(filename, header=0).head(days)
    li.append(df)
frame = pd.concat(li, axis=1)
#print(frame)


#sort dates oldest to newest
frames = frame.sort_index(ascending=False)

#create data frame with only close prices
new_frame = frames[['close']]
print(new_frame)

#daily return of each stock by percent
daily_return = new_frame.pct_change(1)
print(new_frame.pct_change(1))

#Multiply each column of the data frame by the weight ##
data_frame = daily_return.mul(weight_list)
print(data_frame)

#sum returns of stocks for each day
data_row_total = data_frame.sum(axis=1)
print(data_row_total)

#add 1 to the sum of return for each day to calculate cumulative returns
data_sum = data_row_total.add(1)
#print(data_sum)

#print cumulative daily returns
data_frame_cum = data_sum.cumprod()
data_frame_cum_sort = data_frame_cum.sort_index(ascending=True)
print(data_frame_cum)

##calculate ratios

#annual standard deviation
st_dev = data_row_total.values.std() * math.sqrt(252)

#daily return
annual_ret = data_row_total.mean() * 252

#period cumulative return
period_return = data_frame_cum.tail(1) - 1
print(f"Period Return: {percent(float(period_return))}")


#sharpe/skew/kurtosis
sharpe_ratio = annual_ret / st_dev
skew = data_row_total.skew()
kurtosis = data_row_total.kurt()

#Print Results

print (f"Annual Standard Deviation: {percent(float(st_dev))}")
print(f"Annual Return: {percent(float(annual_ret))}")
print(f"Sharpe Ratio: {to_usd(float(sharpe_ratio))}")
print(f"Skew: {to_usd(float(skew))}")
print(f"Kurtosis: {to_usd(float(kurtosis))}")

#plot the cumulative returns over time

plotly.offline.plot({
    "data": [go.Scatter(x=dates, y=data_frame_cum_sort)],
    "layout": go.Layout(title= f"Price Appreciation of $1 Invested in {stock_list}")
}, auto_open=True)



# 