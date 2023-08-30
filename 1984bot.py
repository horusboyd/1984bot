import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents(messages=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='pin', help='pin <message link>')
async def pin_cmd(ctx, message_link: str):
  # server_id = int(link[4]); channel_id = int(link[5]); msg_id = int(link[6])
  message_id = int(message_link.split('/')[6])
  message = await ctx.fetch_message(message_id)
  await message.pin()

@bot.command(name='unpin', help='unpin <message link>')
async def unpin_cmd(ctx, message_link: str):
  message_id = int(message_link.split('/')[6])
  message = await ctx.fetch_message(message_id)
  await message.unpin()

bot.run(token)
