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

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('users.json', 'r', encoding='utf8') as f:
            user = json.load(f)
        try:
            with open('users.json', 'w', encoding='utf8') as f:
                user[str(message.author.id)]['exp'] = user[str(message.author.id)]['exp']+1
                lvl_start = user[str(message.author.id)]['level']
                lvl_end = user[str(message.author.id)]['exp'] ** (1.5/4)
                if lvl_start < lvl_end:
                    user[str(message.author.id)]['level'] = user[str(message.author.id)]['level'] + 1
                    lvl = user[str(message.author.id)]['level']
                    await message.channel.send(f'{message.author.name} leveled up! New level: {lvl}')
                    json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)
                    return
                json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)
        except:
            with open('users.json', 'w', encoding='utf8') as f:
                user = {}
                user[str(message.author.id)] = {}
                user[str(message.author.id)]['level'] = 0
                user[str(message.author.id)]['exp'] = 0
                json.dump(user, f, sort_keys=True, indent=4, ensure_ascii=False)


def setup(bot):
    bot.add_cog(Sandbox(bot))
