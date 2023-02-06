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

        self.upload_channel_id = "YOUR_CHANNEL_ID_HERE"

    @app_commands.command(
        name="meme", description="shows you a random meme from your collection"
    )
    async def meme(self, interaction: discord.Interaction):
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

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id == self.upload_channel_id and message.content == "upload":
            for a in message.attachments:
                if a.filename.endswith(tuple(self.extensions)):
                    await a.save(f"memes/{a.filename}")

                else:
                    await message.channel.send(
                        f"**This file format is not supported, right now!**"
                    )


async def setup(client):
    await client.add_cog(MemeCog(client))
