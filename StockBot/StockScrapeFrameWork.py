# import libs
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime 

#ask for the stock symbol
symbol = input("Enter a stock symbol > ")

quote_page = ('https://www.bloomberg.com/quote/%s:US' % symbol)

#store the webpage in page variable
page = urllib.request.urlopen(quote_page)

#parse the HTML 
soup = BeautifulSoup(page, 'html.parser')

#find name of stock
name_box = soup.find('h1', class_ ='companyName__99a4824b')
#find current price of stock
price_box = soup.find('span', class_ = 'priceText__1853e8a5')
percent_up_down = soup.find()

#name = name_box.text.strip()
print(name_box.text)
#price = price_box.text()
print('$',price_box.text)
