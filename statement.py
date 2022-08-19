import hikari
import requests
from constants import baseUrl

async def Statement(wallet, event: hikari.DMMessageCreateEvent):
    checkWalletUrl = baseUrl + 'statements/' + str(event.author_id)
    print(checkWalletUrl)
    response = requests.get(checkWalletUrl)
    responsejson = response.json()
    print(responsejson)
    await event.message.respond("Wallet Balance: " + str(0))

