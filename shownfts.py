import hikari
import requests
from datetime import datetime
from constants import baseUrl
from table2ascii import table2ascii as t2a, PresetStyle
import base64

async def ShowNFT(wallet, event: hikari.DMMessageCreateEvent):
    showNFTUrl = baseUrl + 'nfts?nft_name=NFTs.' + wallet
    showresponse = requests.get(showNFTUrl)
    showresponsejson = showresponse.json()
    print(showresponsejson)
    statementheader = ["S.No.", "SN" ,"Title","Description", ""]
    nfts = []
    sno = 1
    for trans in showresponsejson['payload']:
        imgdata = base64.b64decode(trans['PNG'])
        filename = str(trans['sn']) + '.PNG'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        with open(filename, "rb") as fh:
            fh = hikari.File(filename)
            #await event.message.respond(fh)
            nfts.append([sno,trans['sn'], trans['hostname'], trans['description'], ''])
        sno = sno + 1
    
    output = t2a(
    header=statementheader,
    body=nfts,
    style=PresetStyle.thin_compact)

    await event.message.respond(f"```\n{output}\n```")
    await event.message.respond('Enter /nft withdraw sn to withdraw NFT')



