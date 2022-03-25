# UDIM Mod API


async def Init(args, message):

    await message.channel.send("Welcome to UDIM! This is the **Ultimate Discord Instant Messaging** Service. Which allows you to\n"
        "Message friends over the UDIM Service system which is a simple, structured, and light system for messaging your friends.\nIt contains WIP mods and such, for you to use.")
    await message.channel.send("`-close <ID>` Closes a running token.\n`DMing the bot` Opens a token in the server.\n`-open` Mounts the server into a listen server\n`-help` This command.")