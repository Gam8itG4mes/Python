import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.xkcd.com/2001'

comic_page = urllib.request.urlopen(url);

soup = BeautifulSoup(comic_page, 'html.parser')

comic_block = soup.findAll('img')

#html_soup = BeautifulSoup(comic_block, 'html.parser')
#html_soup.find('img')

print(comic_block[2].get('title'))
#print(html_soup)