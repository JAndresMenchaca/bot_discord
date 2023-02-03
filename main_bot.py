import json, os
import discord
from discord.ext import commands
TOKEN = "MTA3MDg1NDk3MjQ5MDY2NjA0Ng.Gs0YD0.YvBUXGwiusqjcuiXk0y7J8FylwGetFiRq2L-aY"

def main():
	if os.path.exists("config.json"):
		with open('config.json') as f:
			config_data = json.load(f)
	else:
		template = {'prefix':'!', 'token':TOKEN}
		with open('config.json','w') as f:
			json.dump(template, f)

	prefix = config_data["prefix"]
	token = config_data["token"]
	intents = discord.Intents.all()
	bot = commands.Bot(command_prefix = prefix, intents = intents)

	@bot.command(name="saludar")
	async def saludar(ctx):
		await ctx.reply("Hola, como estas??")


	@bot.event
	async def on_message(message):
		print("recibido")
		autor = message.author
		contenido = message.content
		print("{}".format(contenido))

		if contenido == "hola":
			real_name = str(autor).split("#")
			await message.channel.send('Hello {}!'.format(real_name[0]))

		if contenido == "ping":
			await message.channel.send("Pong")

		await bot.process_commands(message)

	bot.run(token)


if __name__ == "__main__":
	main()








