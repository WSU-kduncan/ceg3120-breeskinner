import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

	for guild in client.guilds:
		if guild.name == GUILD:
			break

	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)

@client.event
async def on_message(message):
	if message.author == client.user:
		return


	barneyStinson_quotes = [
		'It\'s gonna be legen-.... wait for it.... DARY!',
		'When I\'m sad, I just stop being sad and be awesome instead!',
		'In my body, where the shame gland should be there\'s a second awesome gland. True story.',
		'Challenge accepted.',
	]

	if message.content == 'hello!':
		response = random.choice(barneyStinson_quotes)
		await message.channel.send(response)

client.run(TOKEN)
