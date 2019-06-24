import csv
import datetime
import json
import os
#import requests
#import statistics
#import plotly
#import plotly.graph_objs as go

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

stock_list = []
weight_list = []

while True:
    stock_symbol = input("Please enter stock symbol or 'DONE' if complete: ")
    weight = input("Please enter stock weight or 'DONE' if complete example 25 = 25%: ")
    if stock_symbol == "DONE" and weight =="DONE":
        break 
    elif len(stock_symbol) > 5 or weight.isaplha():
     print("Stock symbol input too long or weight is not formatted correctly, expecting a ticker no more than 5 characters and wieght only contains digits")
    elif stock_symbol.isalpha() and weight.isdigit():  
        stock_list.append(stock_symbol)   
        weight_list.append(weight) 
    else: 
        print("Invalid Seletion")

print(stock_list)
print(weight_list)