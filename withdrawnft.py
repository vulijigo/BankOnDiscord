from tokenize import Number
import hikari
import requests
from datetime import datetime
from constants import baseUrl
from table2ascii import table2ascii as t2a, PresetStyle
import base64

async def WithdrawNFT(wallet, event: hikari.DMMessageCreateEvent, sn: Number):
    withdrawNFTUrl = baseUrl + 'nfts/' + sn + '/png'
    print(withdrawNFTUrl)
    nftresponse  = requests.get(withdrawNFTUrl)
    nftresponsejson =nftresponse.json()
    # print(nftresponsejson)
    if(nftresponsejson['status'] == 'error'):
        await event.message.respond(nftresponsejson['payload']['message'])
        return

    if(nftresponsejson['status'] == 'success'):
            data = nftresponsejson['payload']
            # await event.message.respond('Title: ' + data['hostname'])
            # await event.message.respond('Description: ' + data['description'])
            base64txt = data['Data']
            imgdata = base64.b64decode(base64txt)
            filename = str(sn) + '.PNG'
            with open(filename, 'wb') as f:
                f.write(imgdata)
            with open(filename, "rb") as fh:
                fh = hikari.File(filename)
                await event.message.respond(fh)



            

