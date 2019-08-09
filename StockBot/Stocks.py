#import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#specify the url
quote_page  = 'https://www.bloomberg.com/quote/SPX:IND'

#store the webpage HTML in the variable
page = urllib.request.urlopen(quote_page)

#parse the HTML
soup = BeautifulSoup(page, 'html.parser')


name_box = soup.find('h1', attrs={'class':'name'})

name = name_box.text.strip() #strip removes starting and ending spaces
print(name) 

price_box = soup.find('div', attrs = {'class':'price'})
price = price_box.text
print(price)

#put it in a csv file. 'a' is append
with open('S_P_Index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])

