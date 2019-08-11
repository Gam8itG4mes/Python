# import libs
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime 

#ask for the stock symbol
symbol = input("Enter a stock symbol > ")
#symbol = symbol.capitalize()

if symbol == "djia" or symbol == "DJIA":
    quote_page_dji = ('https://www.reuters.com/finance/markets/index/.DJI')
    page_dji = urllib.request.urlopen(quote_page_dji)
    soup = BeautifulSoup(page_dji, 'html.parser')

    name_box_dji = soup.find('div', {'id': 'sectionTitle'})
    price_box_dji = soup.find('div', {'class': 'dataHeader'})
    #change_box_dji = soup.find('div', attrs={'class':'change-container'})

    name_dji = name_box_dji.text.strip()
    print(name_dji)
    price_dji = price_box_dji.text.strip()
    print(price_dji)

elif symbol.upper() == "SPX" or symbol.upper() == "S&P":
    quote_page_spx = ('https://www.reuters.com/finance/markets/index/.SPX')
    page_spx = urllib.request.urlopen(quote_page_spx)
    soup = BeautifulSoup(page_spx, 'html.parser')
   
    name_box_spx = soup.find('div', {'id': 'sectionTitle'})
    price_box_spx = soup.find('div', {'class': 'dataHeader'})
    
    name_spx = name_box_spx.text.strip()
    print(name_spx)
    price_spx = price_box_spx.text.strip()
    print("$" + price_spx)

    
else:
    quote_page = ('https://www.reuters.com/finance/stocks/overview/%s' % symbol)

    #store the webpage in page variable
    page = urllib.request.urlopen(quote_page)

    #parse the HTML 
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)
    #find name of stock
    name_box = soup.find('div', {'id': 'sectionTitle'})
    #find current price of stock
    price_box = soup.find('br', attrs = {'class' : 'clear'})
    #print(price_box.find_next_sibling("span").get_text())
    price_box = price_box.find_next_sibling("span").get_text()
    #percent_up_down = soup.find()

    name = name_box.text.strip()
    #print(name_box.text)
    #name = name_box.text
    print(name)
    price = price_box.strip()
    print('$',price)