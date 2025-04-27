import os
import asyncio
from twitchio.ext import commands

from commands import get_random_verse

class Bot(commands.bot):
    # Construct the bot using our oauth token and channel info.
    def __init__(self):
        info = load_info("./information.txt")
        super().__init__(
            token=info['token'],
            prefix="!",
            initial_channels=info['channel'],
            reconnect=True # Enable auto reconnect.
        )

    # Avoids startup spam.
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        
        # Wait a few seconds before starting up fully
        await asyncio.sleep(2)  # 2 seconds, you can adjust
        print("Bot is fully ready!")

    # Handle disconnect events.
    async def event_disconnect(self):
        print("Bot disconnected! Attempting to reconnect...")

    # Randomly selects a verse from a text file to type in chat.
    @commands.command(name='verse')
    async def verse(self, ctx):
        verse = get_random_verse("./verses.txt")
        await ctx.send(verse)



bot = Bot()
bot.run()
