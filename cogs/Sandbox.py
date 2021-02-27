import discord
from discord.ext import commands
import json


class Sandbox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='hello', aliases=['h', 'he', 'hl'])
    async def hello_command(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command(name='DM')
    async def on_message(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if member == self.bot.user:
            return

        # me = await ctx.fetch_user_profile(ctx.author.id)
        await member.send('Nice')


def setup(bot):
    bot.add_cog(Sandbox(bot))
