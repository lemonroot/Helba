import discord
import os
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
    async def dm_user(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if member == self.bot.user:
            return

        # me = await ctx.fetch_user_profile(ctx.author.id)
        await member.send('Nice')

    @commands.command(name='create')
    async def create(self, ctx):
        directory = ('players/' + str(ctx.author.id) + '/data.json')
        if not os.path.exists('players/{}'.format(ctx.author.id)):
            os.makedirs('players/{}'.format(ctx.author.id))
            new_account = {
                'owner': ctx.author.id,
                'race': 'None',
                'job': 'None',
                'deity': 'None',
                'skill': 'None',
                'lvl': '1',
                'exp': '0',
                'weapon': 'None',
                'armor': 'None',
                'accessory': 'None'
            }

            with open(directory, 'w') as f:
                json.dump(new_account, f)

            print('created')
        else:
            print('exists')
        # json.read(directory)


def setup(bot):
    bot.add_cog(Sandbox(bot))
