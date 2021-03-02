import discord
import os
from discord.ext import commands
from string import ascii_letters, digits, whitespace
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
             'ouka', 'rena', 'shugo', 'lycoris', 'zefie', '.create']
# Please understand that I wouldn't add this without a purpose.

new_account = {
    'owner': 'None',
    'name': 'None',
    'race': 'None',
    'job': 'None',
    'deity': 'None',
    'lvl': '1',
    'exp': '0',
    'weapon': 'None',
    'armor': 'None',
    'accessory': 'None'
}

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

    # Command to create character
    @commands.command(name='create')
    async def _create(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author

        if member == self.bot.user:
            return

        # set owner ID
        new_account['owner'] = str(ctx.author.id)
        await member.send("Welcome to *The World*. The first step in your journey is character creation. We will take "
                          "this one step at a time.")

        time.sleep(2)
        # Name def
        await self._name_check(ctx, member)

        time.sleep(2)
        # Job def
        # await self._job_select(ctx, member)

    # Check if name is forbidden or in use.
    async def _name_check(self, ctx, member):
        await member.send("Let's begin with your **character name**. Reply with a name representing your character. Names "
                          "can be up to 16 characters long, and may include numbers, letters, and spaces.")

        # GET READY FOR SOME MESSY AMATEUR CODE OH BOY OH BOY
        while True:
            try:
                # Name input
                name_try = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                # Length of name
                length = len(str(name_try.content))
                # Test for special characters

                # Grab list of taken names
                file = open('data/namelist.txt', 'r')
                data = file.read().split(',')

                # Check if it's a lore name.
                if name_try.content.lower() in forbidden:
                    await member.send('ERROR: Name is forbidden. Please try again.')
                # Check if it's too long.
                elif length > 16:
                    await member.send('ERROR: Name is too long. Please try again.')
                # Check if it's taken.
                elif name_try.content.lower() in data:
                    await member.send('ERROR: Name is already in use. Please try again.')
                # Check for special characters.
                elif set(name_try.content).difference(ascii_letters + digits + whitespace):
                    await member.send('ERROR: Special characters are not allowed in names.')

                # Nested try statement for name confirmation.
                else:
                    await member.send('You will be known as **' + str(name_try.content) + '**. Is this name acceptable?'
                                                                                          ' Y/N')
                    answer = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                    try:
                        if answer.content.lower() not in ('y', 'yes', 'n', 'no'):
                            await member.send(
                                'You will be known as **' + str(name_try.content) + '**. Is this name acceptable? '
                                                                                    'Please respond with yes or no.')
                        elif answer.content.lower() in ('yes', 'y'):
                            await member.send('Understood. Welcome to *The World*, **' + str(name_try.content) + '**.')
                            # Pass name to account dict
                            new_account['name'] = str(name_try.content)
                            break
                        elif answer.content.lower() in ('no' or 'n'):
                            await member.send("Let's begin with your **character name**. Reply with a name representing "
                                              "your character. Names can be up to 16 characters long, and may include "
                                              "numbers, letters, and whitespace.")
                    except ValueError:
                        await member.send('Unknown error encountered. Please try again.')
            except ValueError:
                await member.send('Unknown error encountered. Please try again.')

"""
    # Select a job.
    async def _job_select(self, ctx, member):
        await member.send('To survive in *The World*, you will need powerful tools at your disposal. Through the use'
                          ' of the **Job** system, you can achieve the impossible. \nFor more information on each job, '
                          'see https://guild.lemonroot.net/jobs.')
        await member.send('When ready, please respond with the name of your desired job (or just the last word in the name).')

        while True:



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
