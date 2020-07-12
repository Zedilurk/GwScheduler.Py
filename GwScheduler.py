import json
import discord
import logging
import time, threading
from GameEventManager import GameEventManager
from CommandManager import CommandManager
from Serializer import Serializer
from datetime import datetime, timedelta

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
eventManager = GameEventManager()
commandManager = CommandManager()

with open('auth.json') as f:
  data = json.load(f)

token = data["token"];

Serializer.LoadFromFile()

print(str(len(GameEventManager.ScheduledEvents)) + " events loaded from .json files")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content[0:1] == '$'):
        command, arguments = commandManager.Parse(message.content[1:])

        commandResponse = commandManager.React(command, message.author.name, arguments)
        await message.channel.send(commandResponse)

        #if message.content.startswith('$hello'):
        #    await message.channel.send('Hello!')

def reset_timer():
    print('Checking reset timers.')
    now = datetime.utcnow()
    anyReset = False

    for gameEvent in GameEventManager.ScheduledEvents:
        if gameEvent.AutoResetRoster:
            if (now == gameEvent.AutoResetTime):
                gameEvent.ResetRoster()
                anyReset = true

    if anyReset:
        Serializer.SaveToFile()

    # get number of seconds until the next hour
    delta = timedelta(hours=1)    
    next_hour = (now + delta).replace(microsecond=0, second=0, minute=2)
    wait_seconds = (next_hour - now).seconds

    # recall this method on the next hour marker
    threading.Timer(wait_seconds, reset_timer).start()


reset_timer()
client.run(token)

# TODO
# Serialization
# Period Backups of Events (to file)
# Event beginning check timer
