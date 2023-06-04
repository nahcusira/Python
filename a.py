import discord
from discord.ext import commands
import requests

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Set up Discord bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot owner ID
bot_owner_id = '1027216124452016188'

# Discord bot event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Discord bot event: Message received
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Send feedback to bot owners
    await send_feedback(message.author, message.content)

    await bot.process_commands(message)

# Send feedback to bot owner
async def send_feedback(author, content):
    bot_owner = await bot.fetch_user(bot_owner_id)
    feedback_message = f'Feedback from {author}: {content}'
    await bot_owner.send(feedback_message)

# Discord bot command: Transfer Fshare link to Google Drive
@bot.command()
async def transfer(ctx, fshare_link):
    # Extract file name from Fshare link
    file_name = fshare_link.split('/')[-1]

    # Download file from Fshare
    try:
        response = requests.get(fshare_link, stream=True)
        response.raise_for_status()

        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        await ctx.send(f'File downloaded from Fshare.')
    except requests.exceptions.RequestException as e:
        await ctx.send(f'Error downloading file from Fshare: {str(e)}')
        return

    # Authenticate and upload file to Google Drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    gfile = drive.CreateFile({'title': file_name})
    gfile.SetContentFile(file_name)
    gfile.Upload()

    # Get Google Drive file URL
    drive_link = gfile['alternateLink']

    # Send Google Drive link to user
    await ctx.send(f'File transferred to Google Drive: {drive_link}')

# Run the bot
bot.run('MTAyNzIxNjEyNDQ1MjAxNjE4OA.GCgsNH.OQoB7sRU9YT1VhsZygxxogGX670y0zOV76F_1M')
