import discord
from discord.ext import commands
import asyncio
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import config


#checks to see if message as sent by the bot
def is_me(m):
    return str(m.author.id) == config.bot_id

#check if message is a command
def is_com(m):
    return m.content.startswith(config.bot_prefix)


class Owner_Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Bot command to delete all messages the bot has made.
    @commands.command(description='Deletes all messages the bot has made')
    @commands.is_owner()
    async def purge(self, ctx):
        """Deletes bot messages and user commands"""
        channel = ctx.message.channel
        deleted = await channel.purge(limit=25, check=is_me)
        deleted1 = await channel.purge(limit=25, check=is_com)
        await ctx.send('Deleted {} command(s)\nDeleted {} message(s)'.format(len(deleted1), len(deleted)))

    #restarts the bot, it jsut closes the connectiona dn relys on an .sh script to restart the python script
    #kinda jank but it works
    @commands.command(description='Restarts Utility Bot')
    @commands.is_owner()
    async def restart(self, ctx):
        """Restarts the Bot."""
        await ctx.send('Restarting Bot. Give it a minute.'.format())
        await self.bot.logout()


    #loads a cog
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def c_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    #unloads a cog
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def c_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    #relaods a cog
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def c_reload(self, ctx, *, cog: str):
        """Command which reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    #lists all the cogs that are currently loaded
    @commands.command(name='list', hidden=True)
    @commands.is_owner()
    async def c_list(self, ctx):
        """tells what cogs have been laoded"""
        try:
            msg = ""
            ext = self.bot.extensions
            for item in ext:
                msg = msg + item + "\n"
            await ctx.send("Extensions Loaded:\n{}".format(msg))
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    #message the server as the bot.
    @commands.command(name='smsg', hidden=True)
    @commands.is_owner()
    async def smessage(self, ctx, cnl,* , msg):
        """message a channel"""
        channel = self.bot.get_channel(int(cnl))
        print(cnl, msg)
        await channel.send(msg)

    #message a person as the bot
    @commands.command(name='pmsg', hidden=True)
    @commands.is_owner()
    async def pmessage(self, ctx, cnl,* , msg):
        """message a person"""
        user = self.bot.get_user(int(cnl))
        print(cnl, msg)
        await user.send(msg)


#add cogs to bot
def setup(bot):
    bot.add_cog(Owner_Cog(bot))
