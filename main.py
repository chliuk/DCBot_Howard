import discord
from discord.ext import commands
import json
import os
import keep_alive
import asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='[', intents=intents)


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
    for filename in os.listdir('cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')


async def main():
    async with bot:
        try:
            if __name__ == "__main__":
                keep_alive.keep_alive()
                await load_extensions()
                await bot.start('OTk4NjA5MjgxMTU2OTE1MjIw.GCanJ8.kP-5AACj0YUAuLLPiWotiMUZLxxsU1Wr45TWGw')
        except:
            os.system("kill 1")


asyncio.run(main())
