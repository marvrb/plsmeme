import discord
from discord.ext import commands
from discord import app_commands

import random
import os
import dotenv



class MemeCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.path = r"memes"  # change this if you change the name of the meme directory
        self.extensions = [
            ".jpg",
            ".png",
            ".jpeg",
        ]  # Sets the allowed file extensions for discord




    @app_commands.command(name='meme', description="shows you a random meme from your collection")
    async def meme(self, interaction:discord.Interaction):

        meme_list = []

        for file in os.listdir(self.path):
            if file.endswith(tuple(self.extensions)):
                meme_list.append(file)

        f = random.choice(meme_list)

        e = discord.Embed()
        file = discord.File(rf"memes/{f}", filename="meme.png")
        e.set_image(url="attachment://meme.png")
        e.set_footer(text=f"created by marv.rb#2404")

        await interaction.channel.typing()
        await interaction.response.send_message(embed=e, file=file)


        
            



async def setup(client):
    await client.add_cog(MemeCog(client))
