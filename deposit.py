from urllib import response
import hikari
import requests
from constants import baseUrl
import os
import json
async def Deposit(wallet, event: hikari.DMMessageCreateEvent):
    checkWalletUrl = baseUrl + 'wallets/' + str(event.author_id) + '?contents=false'
    response = requests.get(checkWalletUrl)
    responsejson = response.json()
    
    if(responsejson['status'] != 'success'):
        print('Wallet does not exist.Creating new one')
        createWalletUrl = baseUrl + 'wallets'
        walletJson = { 'name': str(event.author_id)}
        createresponse = requests.post(createWalletUrl, json= walletJson)
        createresponsejson = createresponse.json()
        print(createresponsejson)
        if(createresponsejson['status'] == 'success'):
            print('Wallet Created successfully')
    print('Depositing', len(event.message.attachments), ' files')
    if (len(event.message.attachments) == 0):
        await event.message.respond('No Coins found')
    else:
        for coin in event.message.attachments:
            fdata = await coin.read()
            filename = os.path.join(os.getcwd() + os.sep + 'import',coin.filename)
            print(filename)
            with open(filename, "wb") as binary_file:
                binary_file.write(fdata)
            depositUrl = baseUrl + 'import'
            depositJson = {"name": str(event.author_id), "items":[{"type":"file", "data":filename}]}
            json_string = json.dumps(depositJson) 
            print(json_string)
            depositresponse = requests.post(depositUrl, json_string)
            depositresponsejson = depositresponse.json()
            if(depositresponsejson['status'] == 'success'):
                await event.message.respond('Coins imported..')
            print(depositresponsejson)

    return ''
