import discord
from discord.ext import commands
import datetime


class Utility(commands.Cog):
    """Utility Commands"""


    def __init__(self, bot):
        self.bot = bot

    #provides information for netwar.
    @commands.command(description='Information for NETWAAR!!')
    async def netwar(self, ctx):
        """NETWAR Information"""
        today = datetime.datetime.today()
        d1 = datetime.datetime(2020, 3, 28, 10, 0, 0)
        d2 = d1 - today
        #create embed
        netwar_info_embed = discord.Embed(
            color=0xff0000,
            description="Information for the NETWAR LAN party.",
            title="NETWAR Information"
        )
        netwar_info_embed.set_image(url="https://www.netwar.org/wp-content/uploads/2018/01/Netwar_Logo.png")

        netwar_info_embed.add_field(
            name="Countdown", value="There is:\n" + str(d2) + " \nuntil Netwar!", inline=True
        )
        netwar_info_embed.add_field(
            name="NETWAR Website", value="https://www.netwar.org/", inline=True
        )
        netwar_info_embed.add_field(
            name="NETWAR Pictures", value="https://flic.kr/s/aHsmGWQyTH", inline=True
        )
        await ctx.send(embed=netwar_info_embed)

    #says hello
    @commands.command(description="say hello to the user")
    async def greet(self, ctx):
        """Says Hello."""
        await ctx.send(":smiley: :wave: Hello, there!")


    #TODO possibly add invite link
    #shows info for the bot
    @commands.command(description="Get info about the Utlity Bot")
    async def info(self, ctx):
        """Shows bot information."""
        embed = discord.Embed(title="Utility Bot", description="Utility Bot for Mayhem servers..", color=0xeee657)

        # give info about you here
        embed.add_field(name="Author", value="Robots_FTW")

        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(self.bot.guilds)}")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite", value="[Invite link](<Not available>)")

        #adds github link for the bot
        embed.add_field(name="GitHub", value="https://github.com/RobotsFTW/NetwarBot")
        await ctx.send(embed=embed)

#adds cog to bot
def setup(bot):
    bot.add_cog(Utility(bot))
