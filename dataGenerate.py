from re import template
from numpy import empty
import yfinance as yf
import pandas as pd

fptr = open("stockList.txt") # opening stocklist file containing codes of stocks
stock_list = [] # creating an empty list to store all stock names

for i in fptr: # iterating through stock list
    stock_list.append(i[:-1]) # removing \n character from the end and appending to the list

temp = yf.download(stock_list[0], start="2016-01-01", end="2022-04-13")
temp["Ticker"] = stock_list[0]
temp.to_csv("dataset.csv")

for i in range(1,len(stock_list)):
    main_file = pd.read_csv("dataset.csv")
    temp = yf.download(stock_list[i], start="2016-01-01", end="2022-04-13")
    if temp.empty:
        continue
    temp["Ticker"] = stock_list[i]
    merged = main_file.append(temp)
    merged.to_csv("dataset.csv")