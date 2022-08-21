import hikari
import requests
from constants import baseUrl

async def Statement(wallet, event: hikari.DMMessageCreateEvent):
    statementUrl = baseUrl + 'wallets/' + wallet + '?contents=true' 
    response = requests.get(statementUrl)
    responsejson = response.json()
    for trans in responsejson['payload']['transactions']:
        await event.message.respond('Date: ' + trans['datetime'] + ',\t Type:' + trans['type'] + '.\t Message: ' + trans['message'] + '.\t Amount: ' + str(trans['amount']))

