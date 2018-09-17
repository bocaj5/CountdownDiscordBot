import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = dicord.client()
client = command.Bot(commands_prefix = "!")

@client.event
async def on_ready
    print("Bot Is Ready")

@client.event
async def on_message(message):
    if message.content == "countdown":
        await client.send_message(message.channel, ":Ready:")



client.run("TOKEN")
