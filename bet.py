from unicodedata import numeric
import hikari
import requests
from constants import baseUrl
import json
import time

async def Bet(wallet, event: hikari.DMMessageCreateEvent, towallet: str, amount, description: str):
    transferUrl = baseUrl + 'transfer'
    print('moving from :'+ str(wallet) + ' to :', towallet, transferUrl )
    moveJson = {'srcname': wallet , 'dstname': towallet , 'amount' : int(amount), 'tag': description}
    json_string = json.dumps(moveJson) 
    print(json_string)
    moveresponse = requests.post(transferUrl, json_string)
    moveresponsejson = moveresponse.json()
    depositstatus = moveresponsejson['payload']['status']
    TASK_URL = baseUrl + 'tasks/' + moveresponsejson['payload']['id']
    while depositstatus == 'running':
        taskresponse = requests.get(TASK_URL)
        taskresponsejson = taskresponse.json()
        depositstatus = taskresponsejson['payload']['status']
        if(depositstatus == 'error'):
            await event.message.respond("Move failed: " + taskresponsejson['payload']['data']['message'])

        time.sleep(1)
        if(depositstatus == 'completed'):
            if(taskresponsejson['status'] == 'success'):
                await event.message.respond("Bet Placed for " + str(taskresponsejson['payload']['data']['amount']) + ' coins ')


