import urllib.request
from bs4 import BeautifulSoup
import random, time



f = open('prev_comics.txt', 'a')
prev_numbers = set(line.rstrip() for line in open("prev_comics.txt"));

#for i in prev_numbers:
#	print(i);

counter = 0;
while counter < 5:
	
	x = random.randint(800, 805);

	url = ('https://www.xkcd.com/%d' % x);
	comic_page = urllib.request.urlopen(url);
	soup = BeautifulSoup(comic_page, 'html.parser')
	comic_block = soup.findAll('img')
	

	#for line in open('prev_comics.txt'):
	if x in prev_numbers:
		print("%d already in set" % x);
	elif x not in prev_numbers:
		f.write('%d\n' % x);
		prev_numbers.add(x);
		print(x);
		print(comic_block[2].get('title'));
		
	#f.write('%d\n' % x);

	
	

	counter += 1;
	time.sleep(30);
#print(html_soup)


