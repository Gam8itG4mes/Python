import discord
import asyncio
import requests
from discord.ext.commands import Bot
from discord import Game
import random 
import urllib.request
from bs4 import BeautifulSoup


TOKEN = 

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix = BOT_PREFIX)

@client.command(name = "8ball", 
				description = "Answers a yes/no question",
				brief = "Answers from the beyond", 
				aliases = ['eight_ball', 'eightball', '8 ball'],
				pass_context = True)

async def eight_ball(context):
	possible_responses = [
		'That is a resounding no.', 
		'It is not looking likely', 
		'Too hard to tell',
		'Definitely'
	]
	await client.say(random.choice(possible_responses) + ', ' +
		context.message.author.mention)
'''
@client.command()
async def square(number):
	sq_val = int(number) * int(number)
	await client.say(str(number) + ' squared is ' + str(sq_val))
'''

@client.event
async def on_ready():
	await client.change_presence(game = Game(name='with Humans'))
	print('logged in as ' + client.user.name)

@client.command()
async def bitcoin():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
	response = requests.get(url)
	value = response.json()['bpi']['USD']['rate']
	await client.say("Bitcoin price is $ " + value)


@client.command(description =  'Returns the stock information for the given stock of the provided NYSE abbreviation',
				brief = 'Provides stock market information',
				aliases = ['stocks'])
async def stock(symbol):
	if symbol == 'SPX':
		quote_page_spx = ('https://www.bloomberg.com/quote/SPX:IND')
		page_spx = urllib.request.urlopen(quote_page_spx)
		soup = BeautifulSoup(page_spx, 'html.parser')

		name_box_spx = soup.find('h1', attrs={'class':'name'})
		price_box_spx = soup.find('div', attrs={'class':'price'})
		change_box_spx = soup.find('div', attrs={'class':'change-container'})

		await client.say(name_box_spx.text.strip())
		await client.say('$' + price_box_spx.text)
		await client.say(change_box_spx.text.strip())
		await client.say(quote_page_spx)

	elif symbol == "INDU" or symbol == "DJIA":
		quote_page_dja = ('https://www.bloomberg.com/quote/INDU:IND')
		page_dja = urllib.request.urlopen(quote_page_dja)
		soup = BeautifulSoup(page_dja, 'html.parser')

		name_box_dja = soup.find('h1', attrs={'class':'name'})
		price_box_dja = soup.find('div', attrs={'class':'price'})
		change_box_dja = soup.find('div', attrs={'class':'change-container'})

		
		await client.say(name_box_dja.text.strip())
		await client.say('$' + price_box_dja.text)
		await client.say(change_box_dja.text.strip())
		await client.say(quote_page_dja)

	else:
		quote_page = ('https://www.bloomberg.com/quote/%s:US' % symbol)
		page = urllib.request.urlopen(quote_page)
		soup = BeautifulSoup(page, 'html.parser')

		name_box = soup.find('h1', class_ ='companyName__99a4824b')
		price_box = soup.find('span', 'priceText__1853e8a5')
		percent_up_down = soup.find('span', class_ = 'changePercent__2d7dc0d2')
		change_box = soup.find('span', class_ = 'changeAbsolute__395487f7')

		
		await client.say(name_box.text)
		await client.say('$' + price_box.text)
		await client.say(change_box.text + " " + percent_up_down.text)
		await client.say(quote_page)

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print('Current servers:')
		for server in client.servers:
			print(server.name)
		await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)