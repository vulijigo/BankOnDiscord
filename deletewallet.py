import hikari
import requests
from constants import baseUrl
import json
async def DeleteWallet(wallet, event: hikari.DMMessageCreateEvent):
    print('Deleting wallet', wallet)
    deleteUrl = baseUrl + 'wallets/' + str(wallet)
    response = requests.delete(deleteUrl)
    responsejson = response.json()
    print(responsejson)
    if(responsejson['status'] == 'success'):
        await event.message.respond('Wallet deleted successfully')
    else:
        await event.message.respond('We could not delete your wallet. Please try again later!!')




