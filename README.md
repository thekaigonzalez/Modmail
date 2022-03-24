<div style="text-align: center">
[UDIM Logo](img/UDiMLogo.png)
</div>

# U.D.I.M

Ultimate Discord Instant Messenger.

UDIM is a bot that allows you to chat remotely, using it's organic system and user management.

* Fast (only implemented in *almost 100* lines of code, while being easy to read)
* Easy to use (Just type `-server` and you'll be ready to go!)
* Reliable (it has been tested to only provide errors if measures aren't taken!)

## How do I use UDIM?

In U.D.I.M 1, You would use

`-server`   In the main server. Any channel.

Then, you would have members DM the bot, which creates a `<USERID>-token` channel.

This is a listen channel, Type any message in it to have it forwarded to the person the channel's for!

To close it, it gives you a command similar to: `-close <USERID>`, That's how you close channels, and reset the value of that user.

## How do I exclude users

There is currently no way to exclude users, but there is a way to automatically *exclude* them after one use.

Create `udim.toml` and write:

```toml
[admin_settings]
excludeAfterUse = true # Exclude so that user can only use modmail once
```

Then run the bot, and after one attempt, they should no longer be able to use UDIM.