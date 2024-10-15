import os
import time
import random
import dotenv
import asyncio

dotenv.load_dotenv()

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", self_bot=True)


@bot.event
async def on_ready():
    print("=======================================")


@bot.command()
async def dankie(ctx):

    await ctx.send("You Need To Cry Dude .....")

    Continue = True
    while Continue:
        await ctx.send("pls highlow")
        message = await bot.wait_for(
            "message", check=lambda m: m.author == 270904126974590976
        )

        print(message.content)

        await message.components[0].children[random.randint(0, 3)].click()

        Continue = False


@bot.event
async def on_message(message):
    if message.author.id == 270904126974590976:
        print(message.content)

    await bot.process_commands(message)


bot.run(os.environ["token"])
