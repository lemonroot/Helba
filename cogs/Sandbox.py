import discord
import os
from discord.ext import commands
import time
import json

forbidden = ['aura', 'balmung', 'blackRose', 'cubia', 'elk', 'gardenia', 'helba', 'kite', 'marlo', 'mia', 'mistral',
             'moonstone', 'natsume', 'nuke usagimaru', 'orca', 'skeith', 'innis', 'magus', 'fidchell', 'gorre', 'macha',
             'tarvos', 'corbenik', 'piros', 'rachel', 'sanjuro', 'tartarga', 'terajima ryoko', 'wiseman', 'aina',
             'alkaid', 'antares', 'atoli', 'asta', 'azure balmung', 'azure kite', 'azure orca', 'bordeaux', 'endrance',
             'gabi', 'gaspard', 'haseo', 'hiiragi', 'iyoten', 'kaede', 'kuhn', 'matsu', 'nala', 'negimaru', 'ovan',
             'pi', 'phyllo', 'piros the 3rd', 'piros the 2nd', 'sakaki', 'sakubo', 'shino', 'silabus', 'sirius',
             'sophora', 'tabby', 'taihaku', 'tri-Edge', 'yata', 'zelkova', 'aika', 'tokio', 'saika', 'albireo', 'bear',
             'tsukasa', 'mimiru', 'bt', 'sora', 'crim', 'silver knight', 'morganna', 'subaru', 'mireille',
             'ouka', 'rena', 'shugo', 'zefie']



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
    async def create(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if member == self.bot.user:
            return

        await member.send('Welcome to The World.')
        time.sleep(2)
        await member.send("Let's begin with your name. Reply with a name representing your character. Names can be up to"
                          "16 characters long, and may include numbers, letters, and spaces.")
        name_try = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if name_try.content.lower() in forbidden:
            await member.send('This name is forbidden. Please try again.')
        else:
            with open('data/namelist.json', 'r') as file:
                data = json.load(file)
            if name_try.content.lower() in data["names"].__str__():
                await member.send('Name is taken. Please try again.')
            await member.send('This works.')



"""
        new_account = {
            'owner': ctx.author.id,
            'race': 'None',
            'job': 'None',
            'deity': 'None',
            'lvl': '1',
            'exp': '0',
            'weapon': 'None',
            'armor': 'None',
            'accessory': 'None'
        }
        directory = ('players/' + str(ctx.author.id) + '/profile1/info.json')

        if not os.path.exists('players/{}'.format(ctx.author.id)):
            os.makedirs('players/{}'.format(ctx.author.id) + '/profile1')

            with open(directory, 'w') as f:
                json.dump(new_account, f)

            print('created profile 1')
        else:
            if not os.path.exists('players/{}'.format(ctx.author.id) + '/profile2'):
                os.makedirs('players/{}'.format(ctx.author.id) + '/profile2')
                directory = ('players/' + str(ctx.author.id) + '/profile2/info.json')

                with open(directory, 'w') as f:
                    json.dump(new_account, f)
                print('created profile 2')

            else:
                print('both slots filled!')
        # json.read(directory)
"""


def setup(bot):
    bot.add_cog(Sandbox(bot))
