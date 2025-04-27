import os
from twitchio.ext import commands

from commands import get_random_verse

class Bot(commands.bot):

    def __init__(self):
        # First get our 
        INFO = []
        with open("./token.txt", 'r', encoding='utf-8') as f:
            for line in f:
                INFO.append(line)

        # Then we construct our bot class using that token
        super().__init__(
            token=INFO[0],
            prefix="!",
            initial_channels=[INFO[1]]
        )

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    # Randomly selects a verse from a text file to type in chat.
    @commands.command(name='verse')
    async def verse(self, ctx):
        verse = get_random_verse("./verses.txt")
        await ctx.send(verse)


bot = Bot()
bot.run()
