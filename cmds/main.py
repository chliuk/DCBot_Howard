import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

<<<<<<< HEAD
=======

>>>>>>> 089c665 (data record before 20240227)
class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
<<<<<<< HEAD
    

async def setup(bot):
    await bot.add_cog(Main(bot))
=======


async def setup(bot):
    await bot.add_cog(Main(bot))
>>>>>>> 089c665 (data record before 20240227)
