import os


async def OnPeerForwarded(IRequester, Token):
    await Token.send("Hello!")