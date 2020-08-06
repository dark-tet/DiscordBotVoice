import os
import discord
from discord.ext import commands

headlogo = 'https://i.imgur.com/4kqeG8A.gif'
footerlogo = 'https://i.imgur.com/2MIe4pt.png'

client = commands.Bot(command_prefix=';')
client.remove_command('help')


@client.command()
async def help(ctx):
    embed = discord.Embed(color=0x00fff9)
    embed.set_author(name=' ឵឵ ', icon_url=headlogo)
    embed.add_field(name='**restart**', value='Restart Cogs', inline=False)
    embed.add_field(name='**hi**', value='hellow', inline=False)
    embed.add_field(name='**print**', value='Print something', inline=False)
    embed.add_field(name='**help**', value='Show this menu', inline=False)
    await ctx.send(embed=embed)


@client.command()
async def restart(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} Reastart Successfully Complete :yum:')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# ultracraft.remove_command('help')


print('Bot Online')
client.run('token')
