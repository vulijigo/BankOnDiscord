import hikari
import requests
from datetime import datetime
from constants import baseUrl
from table2ascii import table2ascii as t2a, PresetStyle

async def Statement(wallet, event: hikari.DMMessageCreateEvent):
    statementUrl = baseUrl + 'wallets/' + wallet + '?contents=true' 
    print(statementUrl)
    response = requests.get(statementUrl)
    responsejson = response.json()
    statementheader = ["S.No." ,"Date","Type", "Description", "Amount", "Running Balance"]
    records = []
    if(responsejson['status'] == 'error'):
        if(responsejson['payload']['message'] == 'Wallet not found'):
            await event.message.respond('No statements')        
    sno = 1
    for trans in responsejson['payload']['transactions']:
        date = trans['datetime'].split('T')
        records.append([sno, date[0],trans['type'], trans['message'], trans['amount'], trans['running_balance']])

    output = t2a(
    header=statementheader,
    body=records,
    style=PresetStyle.thin_compact)

    await event.message.respond(f"```\n{output}\n```")



