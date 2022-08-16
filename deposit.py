from urllib import response
import hikari
import requests
from constants import baseUrl
import os
async def Deposit(wallet, event: hikari.DMMessageCreateEvent):
    checkWalletUrl = baseUrl + 'wallets/' + str(wallet) + '?contents=false'
    response = requests.get(checkWalletUrl)
    responsejson = response.json()
    if(responsejson['payload']['message'] == 'Wallet not found'):
        print('Wallet does not exist.Creating new one')
        createWalletUrl = baseUrl + 'wallets'
        walletJson = { 'name': str(wallet)}
        createresponse = requests.post(createWalletUrl, json= walletJson)
        createresponsejson = createresponse.json()
        if(createresponsejson['status'] == 'success'):
            print('Wallet Created successfully')
    print('Depositing', len(event.message.attachments), ' files')
    if (len(event.message.attachments) == 0):
        await event.message.respond('No Coins found')
    else:
        for coin in event.message.attachments:
            fdata = await coin.read()
            filename = os.path.join(os.getcwd() + '\\import',coin.filename)
            print(filename)
            with open(filename, "wb") as binary_file:
                binary_file.write(fdata)
            depositUrl = baseUrl + 'import'
            depositJson = {'name': str(wallet), 'items':[{'type':'file', 'data':filename}]}
            print(depositJson)
            depositresponse = requests.post(depositUrl, depositJson)
            depositresponsejson = depositresponse.json()
            print(depositresponsejson)

    return ''
