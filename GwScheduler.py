import discord
import logging
import GameEventManager
import CommandManager

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

eventManager = GameEventManager.GameEventManager()
commandManager = CommandManager.CommandManager()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content[0:1] == '$'):
        command, arguments = commandManager.Parse(message.content[1:])
        commandManager.React(command, arguments)

    #if message.content.startswith('$hello'):
    #    await message.channel.send('Hello!')

client.run('NzI3MzI1MTg5MjAwOTM3MDcx.XwUadQ.GRaCEyX8H9VFOR6S3IXpw11Ad1s')


# TODO
# GameEvent class
# Serialization
# Period Backups of Events (to file)
# Event beginning check timer