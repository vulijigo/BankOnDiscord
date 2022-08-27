import hikari
import requests
from datetime import datetime
from constants import baseUrl

async def CreateNFT(wallet, event: hikari.DMMessageCreateEvent, title: str, desc: str):
    print('Creating NFT')