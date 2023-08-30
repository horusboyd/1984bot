import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='pin', help='pin <message link>')
async def pin_cmd(ctx, message_id: int):
  message = await ctx.fetch_message(message_id)
  await message.pin()

@bot.command(name='unpin', help='unpin <message link>')
async def pin_cmd(ctx, message_id: int):
  message = await ctx.fetch_message(message_id)
  await message.unpin()

bot.run(token)

