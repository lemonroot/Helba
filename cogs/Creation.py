import discord
from discord.ext import commands
import json


class Creation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

def setup(bot):
    bot.add_cog(Creation(bot))