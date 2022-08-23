import hikari
import requests
from constants import baseUrl

async def MyWallet(wallet, event: hikari.DMMessageCreateEvent):
    await event.message.respond(str(wallet))
    
