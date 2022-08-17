from ast import While
from urllib import response
import hikari
import requests
from constants import baseUrl
import os
import json
import time
from showcoins import ShowCoins
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
    await event.message.respond('Starting Coins deposit...')
    if (len(event.message.attachments) == 0):
        await event.message.respond('No Coins found')
    else:
        for coin in event.message.attachments:
            fdata = await coin.read()
            filename = os.path.join(os.getcwd() + os.sep + 'import',coin.filename)
            print(filename)
            await event.message.respond('Processing file: ' + coin.filename)
            with open(filename, "wb") as binary_file:
                binary_file.write(fdata)
            depositUrl = baseUrl + 'import'
            depositJson = {"name": str(event.author_id), "items":[{"type":"file", "data":filename}]}
            json_string = json.dumps(depositJson) 
            print(json_string)
            depositresponse = requests.post(depositUrl, json_string)
            depositresponsejson = depositresponse.json()
            depositstatus = depositresponsejson['payload']['status']
            TASK_URL = baseUrl + 'tasks/' + depositresponsejson['payload']['id']
            print(TASK_URL)
            while depositstatus == 'running':
                taskresponse = requests.get(TASK_URL)
                taskresponsejson = taskresponse.json()
                depositstatus = taskresponsejson['payload']['status']
                time.sleep(2)
            if(depositstatus == 'completed'):
                authentic = taskresponsejson['payload']['data']['pown_results']['authentic']
                counterfeit = taskresponsejson['payload']['data']['pown_results']['counterfeit']
                total = taskresponsejson['payload']['data']['pown_results']['total']
                unknown = taskresponsejson['payload']['data']['pown_results']['unknown']
                await event.message.respond('Coins imported..\nTotal: ' + str(total) + '\nAuthentic: '+ str(authentic) + '\nCounterfeit:' + str(counterfeit) + '\nUnknown: ' + str(unknown))
            await ShowCoins(wallet, event)

    return ''
