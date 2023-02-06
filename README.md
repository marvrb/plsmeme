<p align="center"><a href="https://github.com/marvrb/plsmeme"><img src="https://thumbs.gfycat.com/AgitatedLiveAgouti.webp" width="400"><a/></p>

#  <p align="center">plsmeme<p/><p align="center"><img src="https://img.shields.io/badge/License-MIT-blue"> <img src="https://img.shields.io/pypi/pyversions/discord.py?label=Python&logo=python&logoColor=FFD43B"><p/>
<p align="center">The meme bot for your personal memes!<p/>

<p align="center">Just post your memes in the /meme folder and your ready to go.<p/>

<br>


**.env (config)**
```shell

TOKEN=YOUR_TOKEN_HERE

(replace "YOUR_TOKEN_HERE" with your own bot token)
```

<br>

**cogs/meme.py**
```shell

   def __init__(self, client):
       self.client = client
       self.path = r"memes"  # change this if you change the name of the meme directory
       self.extensions = [
           ".jpg",
           ".png",
           ".jpeg",
       ]  # Sets the allowed file extensions for discord
       self.upload_channel_id = "YOUR_CHANNEL_ID_HERE"
       
   (CHANGE THE "self.upload_channel_id" ELSE IT WILL NOT WORK)

```

<br>

## Features:

|Feature| Explanation |
|--|--|
| upload | let's you upload your own memes over a discord channel directly into the **/meme** older|

<br>

## To-Do's:
 - [x] 📩 Upload channel
