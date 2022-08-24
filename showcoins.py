import hikari
import requests
from constants import baseUrl

async def ShowCoins(wallet, event: hikari.DMMessageCreateEvent):
    checkWalletUrl = baseUrl + 'wallets/' + wallet
    response = requests.get(checkWalletUrl)
    responsejson = response.json()
    if(responsejson['status'] == 'success'):
        await event.message.respond("Wallet Balance: " + str(responsejson['payload']['balance']))
    else:
        await event.message.respond("Wallet Balance: " + str(0))

    embed = hikari.Embed()
    embed.title = "Wallet Name: " + str(wallet)

    embed.description = "Wallet Balance: 0"
    ch = event.message.fetch_channel
    hikari.File('')
    
