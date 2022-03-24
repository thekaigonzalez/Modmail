import json
import os
import pathlib
import discord
import toml
from discord.ext import commands

EXCLUDE_AFTER_USE = False
SAVE_VALUES_ON_EXIT = False
if pathlib.Path("udim.toml").exists():
    t = toml.load('udim.toml')
    EXCLUDE_AFTER_USE = t['admin_settings']["excludeAfterUse"]
class Bot(commands.Bot):
    async def async_cleanup(self):  # example cleanup function
        print("Exiting...")
            
    async def close(self):
        # do your cleanup here
        await self.async_cleanup()
        
        await super().close()  # don't forget this!

client = Bot(command_prefix="-")

@client.event
async def on_ready():
    users = {}
    extras = {}
    exclude = []

def find_user_from_users(id):
    for m in users:
        if m == id: return (True, id)
        else: continue
    return (False, None)

def get_token_channel_id(id):
    ch = None

    for i in tokchan.channels:
        if i.name == id + "-token":
            ch = i
    return ch

@client.event
async def on_message(msg: discord.Message):
    global exclude
    global user
    global extras
    global users
    global send1er
    global tokchan
    try:
            users
    except Exception:
            users = {}
    try:
            extras
    except Exception:
            extras = {}

    try:
            exclude
    except Exception:
            print("reset")
            exclude = []
   
    if msg.author == client.user: return
    if msg.content.startswith("-"):
        content = msg.content[msg.content.find("-")+1:]
        args = []
        b = ""
        state = 0
        for char in content:
            if char == '"' and state == 0:
                state = 5
            elif char == '"' and state == 5: state = 0
            elif char == ' ' and state == 0:
                args.append(b)
                b = ""
            else:
                b += char
        if len(b) != 0:
            if state == 0:
                args.append(b)
        if not msg.guild:
            if args[0] == 'open' and not msg.guild:
                await msg.channel.send("You are now connected to a ticket channel. **Say hi!**")
                user = msg.author
        if args[0] == 'server' and msg.guild:
            await msg.channel.send("This is now the main server for recieving ModMail messages.")
            
            tokchan = msg.guild
        if args[0] == 'close':
            exclude.append(args[1])
            if get_token_channel_id(args[1]) != None:
                
                await msg.channel.delete()
                del extras[args[1]]
                del users[msg.channel.id]
                


    f,i = find_user_from_users(str(msg.author.id))
    if not msg.guild and get_token_channel_id(str(msg.author.id)):
        await get_token_channel_id(str(msg.author.id)).send(msg.content)
    
    if not msg.guild and extras.get(str(msg.author.id)) == None:
        if str(msg.author.id) in exclude:
            print("Excluded")
            await msg.channel.send("You can not send another modmail. `EXCLUDE_AFTER_CLOSE` is enabled.")
            return
        await tokchan.create_text_channel(str(msg.author.id) + "-token")
        ch = None

        for i in tokchan.channels:
            if i.name == str(msg.author.id) + "-token":
                print("FOUND")
                ch = i
                break
        idx = str(ch.id)

        users[idx] = msg.author
        extras[str(msg.author.id)] = msg.channel

        await msg.channel.send("You're on! **Say hi!**")
        await ch.send("User: " + msg.author.display_name + "\nCommand to remove token: " + "`-close " + str(msg.author.id) + "`")
    
    if users.get(str(msg.channel.id)) != None:
        await extras[str(msg.author.id)].send(msg.content)

token = open("token.txt", "r")
client.run(token.read().strip())
token.close()