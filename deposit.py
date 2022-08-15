from urllib import response
import requests
from constants import baseUrl
async def Deposit(wallet):
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
    return ''
