import discord
import asyncio
import requests
from discord.ext.commands import Bot
from discord import Game
import random 
import urllib.request
from bs4 import BeautifulSoup


TOKEN = #insert discord token

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
	await context.send(random.choice(possible_responses) + ', ' +
		context.message.author.mention)
'''
@client.command()
async def square(number):
	sq_val = int(number) * int(number)
	await client.send(str(number) + ' squared is ' + str(sq_val))
'''

@client.event
async def on_ready():
	game = discord.Game("with the humans")
	await client.change_presence(discord.Status.online, activity = game)
	#await client.change_presence(game = Game(name='with Humans'))
	print('logged in as ' + client.user.name)


@client.command()
async def bitcoin():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
	response = requests.get(url)
	value = response.json()['bpi']['USD']['rate']
	await client.send("Bitcoin price is $ " + value)


@client.command(description =  'Returns the stock information for the given stock of the provided NYSE abbreviation',
				brief = 'Provides stock market information',
				aliases = ['stocks'])
async def stock(self, symbol):
	#symbol = symbol.upper()
	if symbol == 'SPX' or symbol.upper() == "S&P":
		quote_page_spx = ('https://www.reuters.com/finance/markets/index/.SPX')
		page_spx = urllib.request.urlopen(quote_page_spx)
		soup = BeautifulSoup(page_spx, 'html.parser')

		name_box_spx = soup.find('div', {'id':'sectionTitle'})
		price_box_spx = soup.find('div', {'class':'dataHeader'})
		#change_box_spx = soup.find('div', {'class':'change-container'})

		await self.send(name_box_spx.text.strip())
		await self.send('$' + price_box_spx.text.strip())
		#await self.send(change_box_spx.text.strip())
		#await self.send(quote_page_spx)

	elif symbol == "INDU" or symbol == "DJIA":
		quote_page_dja = ('https://www.reuters.com/finance/markets/index/.DJI')
		page_dja = urllib.request.urlopen(quote_page_dja)
		soup = BeautifulSoup(page_dja, 'html.parser')

		name_box_dja = soup.find('div', {'id':'sectionTitle'})
		price_box_dja = soup.find('div', {'class':'dataHeader'})
		#change_box_dja = soup.find('div', attrs={'class':'change-container'})

		
		await self.send(name_box_dja.text.strip())
		await self.send('$' + price_box_dja.text.strip())
		#await self.send(change_box_dja.text.strip())
		#await self.send(quote_page_dja)

	else:
		quote_page = ('https://www.reuters.com/finance/stocks/overview/%s' % symbol)
		page = urllib.request.urlopen(quote_page)
		soup = BeautifulSoup(page, 'html.parser')

		name_box = soup.find('div', {'id': 'sectionTitle'})
		price_box = soup.find('br', attrs = {'class' : 'clear'})
		print("im in the else statement now")
		print(quote_page)
		price_box = price_box.find_next_sibling("span").get_text()
		#percent_up_down = soup.find('span', class_ = 'changePercent__2d7dc0d2')
		#change_box = soup.find('span', class_ = 'changeAbsolute__395487f7')

		name = name_box.text.strip()
		await self.send(name)
		price = price_box.strip()
		await self.send('$' + price)
		#await symbol.send(change_box.text + " " + percent_up_down.text)
		#await symbol.send(quote_page)

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print('Current servers:')
		for server in client.servers:
			print(server.name)
		await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
