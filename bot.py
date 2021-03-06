import discord
import config
from discord.ext import commands
import config
import datetime


#cog list
initial_extensions = ['cogs.utility',
                      'cogs.owner',
                      'cogs.help']

#create bot
bot = commands.Bot(command_prefix=config.bot_prefix, case_insensitive=True)

#remove default help command since we are adding our own.
bot.remove_command('help')


#load cogs
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
        print("loaded: {}".format(extension))


#prints bot info in terminal to let you know it's on.
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Servers:")
    for item in bot.guilds:
        print("  {}".format(item))
    print('------')
    activity = discord.Game("{}help for commands".format(config.bot_prefix))
    await bot.change_presence(status=discord.Status.online, activity=activity)


#sends errors, mainly going to be command not found errors.
@bot.event
async def on_command_error(ctx, error):
    await ctx.send("error: {}".format(error))


#prints when the bot has dropped connection to discord's api.
@bot.event
async def on_disconnect():
    print("Disconnected: {}".format(datetime.datetime.now()))


#run bot
bot.run(config.bot_key)
