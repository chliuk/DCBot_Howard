import discord
from discord.ext import commands
import json
import os
import asyncio

<<<<<<< HEAD
with open('/DiscordBot/BotProject01/setting.json','r',encoding='utf8') as jfile:
=======
with open('setting.json','r',encoding='utf8') as jfile:
>>>>>>> 089c665 (data record before 20240227)
    jdata = json.load(jfile)


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online<<")



@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done')    

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done')



async def load_extensions():
<<<<<<< HEAD
    for filename in os.listdir('/DiscordBot/BotProject01/cmds'):
=======
    for filename in os.listdir('cmds'):
>>>>>>> 089c665 (data record before 20240227)
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

async def main():
    async with bot:
        if __name__ == "__main__":
            await load_extensions()
            await bot.start(jdata['TOKEN'])


asyncio.run(main())
    