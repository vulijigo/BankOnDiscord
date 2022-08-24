import hikari
import requests
from constants import baseUrl
import json
import time
import os

async def Transfer(wallet, event: hikari.DMMessageCreateEvent, amount: int, skywallet: str):
    print('transferring from ', str(wallet) , ' to ', skywallet, ' ' ,str(amount) , ' Cloudcoins' )
    depositUrl = baseUrl + 'deposit'
    moveJson = {'name': str(wallet) , 'toname': skywallet , 'amount' : int(amount), 'tag': ''}
    json_string = json.dumps(moveJson) 
    moveresponse = requests.post(depositUrl, json_string)
    moveresponsejson = moveresponse.json()
    depositstatus = moveresponsejson['payload']['status']
    TASK_URL = baseUrl + 'tasks/' + moveresponsejson['payload']['id']

    while depositstatus == 'running':
        taskresponse = requests.get(TASK_URL)
        taskresponsejson = taskresponse.json()
        depositstatus = taskresponsejson['payload']['status']
        if(depositstatus == 'error'):
            await event.message.respond("Transfer failed: " + taskresponsejson['payload']['data']['message'])

        time.sleep(1)
        if(depositstatus == 'completed'):
            if(taskresponsejson['status'] == 'success'):
                await event.message.respond("Move completed: " + str(amount) + ' coins moved to ' + skywallet)
    
