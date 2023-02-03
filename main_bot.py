import json, os
import discord
from discord.ext import commands
from discord.utils import get
TOKEN = ""

def main():
	if os.path.exists("config.json"):
		with open('config.json') as f:
			config_data = json.load(f)
	else:
		template = {'prefix':'mp!', 'token':TOKEN}
		with open('config.json','w') as f:
			json.dump(template, f)

	prefix = config_data["prefix"]
	token = config_data["token"]
	intents = discord.Intents.all()
	bot = commands.Bot(command_prefix = prefix, intents = intents)

	@bot.command(name="saludar")
	async def saludar(ctx):
		await ctx.reply("Hola, como estas??")

	@bot.command(name="suma")
	async def suma(ctx, arg1, arg2):
		suma = int(arg1) + int(arg2)
		await ctx.send(suma)

	@bot.command(name="helpme")
	async def helpme(ctx):
		embed = discord.Embed(title="Bot de Ayuda", description="Aqui estan los comandos")
		embed.add_field(name="mp!ping", value="Responde pong")
		await ctx.send(content=None, embed = embed)

	@bot.command(name="conect", pass_context = True)
	async def come(ctx):

		try:
			channel = ctx.message.author.voice.channel

			voice = get(bot.voice_clients, guild=ctx.guild)

			if voice and voice.is_connected():
				await voice.move_to(channel)
			else:
				voice = await channel.connect()
		except:
			await ctx.send("No estas conectado a un canal de voz")

	@bot.command(pass_context = True)
	async def disconect(ctx):
		channel = ctx.message.author.voice.channel
		voice = get(bot.voice_clients, guild = ctx.guild)
		await voice.disconnect()




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

	@bot.event
	async def on_ready():
		await bot.change_presence(activity= discord.Game(name="jugando en el servidor"))



	bot.run(token)


if __name__ == "__main__":
	main()








