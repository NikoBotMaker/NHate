import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = 'NDkwODA5NzgzMDc5NjY1NjY0.DoivRA.2xtkwbG9QnH0hQ9v3qrOSriXs60'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('^hey'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
		
    if message.content.startswith('^NIKO'):
        msg = '{0.author.mention} Wants To You To Die @N I K O'.format(message)
        await client.send_message(message.channel, msg)
		
    if message.content.startswith('^nut'):
        msg = '{0.author.mention} Just Nutted Uncontrollably :peanuts:'.format(message)
        await client.send_message(message.channel, msg)
		
    if message.content.startswith('help'):
        msg = 'If You Would Like A List Of Commands Use the ^cmds Command \nIf You Still Need Help Type Help 2'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('refuse'):
        msg = 'your not allowed to refuse'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('Refuse'):
        msg = 'your not allowed to refuse'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^expose'):
        msg = 'N I K O Does Want Anyone To See This Photo  - https://ibb.co/kPXB1p -'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^Poll'):
        msg = "What Is Better Chocolate Or Caramel \nonly vote once \n:heart: is for chocolate and :yellow_heart: is caramel".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Help 2'):
        msg = "```diff\n-Are you stupid all this bot does is commands just use the ^cmds command\n```".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^cmds'):
        msg = "```fix\n-Command List-\n^NIKO - Hate\n^hey - Says Hi To The Bot\n^nut - Nuts\n^Expose - Exposes Niko Dont Use\n^2\n\n\n<            <<1>>            >\n```".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^2'):
        msg = "```fix\n-Command List-\nNothing is here yet\n<            <<2>>            >\n```".format(message)
        await client.send_message(message.channel, msg)
		
    if message.content.startswith('^Hugs'):
        msg = '->hug @mccarnival#3789 \n->hug @IceTea#1690 \n->hug @Brigette#1316 \n->hug @endercreeperyt#7584 '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('no'):
        msg = 'Shut Up Yes'.format(message)
        await client.send_message(message.channel, msg)

    if ('yes') in message.content:
        msg = 'Ok'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('married'):
        msg = 'Yeah Bitch Hes Married'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Shoulders'):
        msg = 'Shut Up Now'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('shoulders'):
        msg = 'Shut Up Now'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('Shoulders'):
        msg = 'Shut Up Now'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.endswith('shoulders'):
        msg = 'Shut Up Now'.format(message)
        await client.send_message(message.channel, msg)

    if ('Nigger') in message.content:
        await client.delete_message(message)

    if ('nigger') in message.content:
        await client.delete_message(message)

    if ('Bitch') in message.content:
        await client.delete_message(message)

    if ('bitch') in message.content:
        await client.delete_message(message)

    if ('BITCH') in message.content:
        await client.delete_message(message)

    if ('Whore') in message.content:
        await client.delete_message(message)

    if ('whore') in message.content:
        msg = 'Dont say that'.format(message)
        await client.delete_message(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^Coinflip'):
        randomlist = ['Heads','Tails']
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content.startswith('^Salute'):
        randomlist = [':b:abe',':b:ad Gorl',':b:erries']
        await client.send_message(message.channel,(random.choice(randomlist)))

@client.event
async def on_ready():
    print('Niko Hate?')
    print('Has Been Activated')
    print('Calculating %0')
    print('---')
    print('Calculating %5')
    print('---')
    print('Calculating %10')
    print('---')
    print('Calculating %15')
    print('---')
    print('Calculating %20')
    print('---')
    print('Calculating %25')
    print('---')
    print('Calculating %30')
    print('---')
    print('Calculating %35')
    print('---')
    print('Calculating %40')
    print('---')
    print('Calculating %45')
    print('---')
    print('Calculating %50')
    print('---')
    print('Calculating %55')
    print('---')
    print('Calculating %60')
    print('---')
    print('Calculating %65')
    print('---')
    print('Calculating %70')
    print('---')
    print('Calculating %75')
    print('---')
    print('Calculating %80')
    print('---')
    print('Calculating %85')
    print('---')
    print('Calculating %90')
    print('---')
    print('Calculating %95')
    print('---')
    print('Calculating %100')
    print('---')
    print('Finished Bot Is Now Usable')
    print('------')

client.run(TOKEN)
