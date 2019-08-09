# Import necessary packages

from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#using xpath get a list of buyers
#<div title = "buyer-name">Carson Busses</div>
buyers = tree.xpath('//div[@title="buyer-name"]/text()')

#list of prices
#<span class = "item price">$29.95</span>
prices = tree.xpath('//span[@class="item-price"]/text()')
print("Buyers: ", buyers)
print("Prices: ", prices)
