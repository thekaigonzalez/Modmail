# UDIM Developer Documentation

UDIM is a discord modmail, telephone-inspired service, which takes a simpler approach to creating complex discord applications.

## How Listening Works

Listen channels are calculated by a certain array in memory, meaning that:

instead of setting a new thread for listening, it will try to recognize the channel in command-time.

This removes the dependency for asynchronous threading, while also being fast and easy to understand.

##  How queueing works

Queueing works by putting users into an array, and handling the array values.

There will always be TWO arrays: member: channel and channel: member, in case any reverse access needs to happen.

It will add and try to chcek if the user is currently on a live session, then send a message back and forth between the host [Listen channel](#how-listening-works) and the [Reciever](#sender--reciever)

## Sender & Reciever

When two people connect, it is a dummy connection; meaning that as soon as you connect to each other, you're not really connected in a dedicated thread.

Essentially, you are in two channels listening to messages to one another.

Processing is done on_message, and not forever.

