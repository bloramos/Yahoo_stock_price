import requests
import urllib 
from urllib.request import urlopen
from bs4 import BeautifulSoup

stock_name = input ("Enter the stock symbol: ")

url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"

html = urlopen(url)

contents = html.read()
#Create Soup object
soup = BeautifulSoup(contents, 'html.parser')
#define first part of the html structure (main header)
header_yahoo = soup.find(id='quote-header-info')
#find in the previous object "header_yahoo" the where the price is located
stock_value = header_yahoo.find('div', class_='D(ib) Va(m) Maw(65%) Ov(h)')
#print the value
print(f'Stock value of: {stock_name} is : {stock_value.text.strip()} hitpoints')

