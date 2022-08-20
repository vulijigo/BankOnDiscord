import hikari
import requests
from constants import baseUrl
from move import Move
async def Pay(wallet, event: hikari.DMMessageCreateEvent, amount):
    await Move(wallet=wallet, event= event, towallet='Default', amount=amount)

