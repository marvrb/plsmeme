import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
from colorama import Fore, Back, Style


load_dotenv()

class aclient(commands.Bot):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.all(), command_prefix='.')

        self.initial = [
            "cogs.meme",
        ]

    async def setup_hook(self):
        for ext in self.initial:
            await self.load_extension(ext)
        await client.tree.sync()

    async def on_ready(self):
        print(f"{Fore.MAGENTA}{self.user}{Style.RESET_ALL} started!")
        print(f"My Github profile: {Fore.CYAN}https://github.com/marvrb{Style.RESET_ALL}")


client = aclient()
client.run(os.getenv("TOKEN"))


