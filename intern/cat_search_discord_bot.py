import discord
from discord.ext import commands, tasks
from discord.embeds import *
import requests


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def cat(ctx):
    embed = discord.Embed() 
    open('tmp.png', 'wb').write(requests.get('https://cataas.com/cat').content)
    file = discord.File("tmp.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


@bot.event
async def on_message(message):
    if message.content == 

@tasks.loop(minutes=5)
async def send_message():
    channel = bot.get_channel('1025230130806784013')
    embed = discord.Embed()
    open('tmp.png', 'wb').write(requests.get('https://cataas.com/cat').content)
    file = discord.File("tmp.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    channel = await bot.fetch_channel('1025230130806784013')
    await channel.send(file=file, embed=embed)
@bot.event
async def on_ready():
    send_message.start()


bot.run("MTAyNTI0NTc4MTk4MjE5NTc1Mw.GLBt73.3C26CBocjD4NsF-phvhckD0SPHjknVKBxGA8jo")