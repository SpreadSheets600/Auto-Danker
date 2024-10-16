import os
import time
import random
import dotenv
import asyncio
import traceback

dotenv.load_dotenv()

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", self_bot=True)


@bot.event
async def on_ready():
    print("=======================================")


@bot.event
async def on_message(message):
    if message.author.id == 270904126974590976:
        try:

            if message.embeds:

                if (
                    hasattr(message.embeds[0].author, "name")
                    and "SOHAM's high-low game".lower()
                    in message.embeds[0].author.name.lower()
                ):
                    if message.components:
                        await message.components[0].children[
                            random.randint(0, 2)
                        ].click()
                        print("[ + ] Played High Low Game")

                elif (
                    hasattr(message.embeds[0], "description")
                    and "**Where do you want to search?**".lower()
                    in message.embeds[0].description.split("\n")[0].lower()
                ):
                    if message.components:
                        await message.components[0].children[
                            random.randint(0, 2)
                        ].click()
                        print("[ + ] Played Search Game")

        except Exception as e:
            print("[ - ] Error With Message Loading")
            print("\n", e)

            if message.embeds:
                print(message.embeds[0].to_dict())

    await bot.process_commands(message)


bot.run(os.environ["token"])
