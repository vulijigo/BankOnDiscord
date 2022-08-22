from fileinput import close
import hikari
import requests
from constants import baseUrl
import json
import os
import time

async def Withdraw(wallet, event: hikari.DMMessageCreateEvent, amount):
    foldername = os.path.join(os.getcwd() + os.sep + 'export' + os.sep, str(wallet))
    if(not os.path.exists(foldername)):
        os.mkdir(foldername)
    withdrawUrl = baseUrl + 'export'
    moveJson = {'name': wallet , 'type': 'png' , 'amount' : int(amount), 'tag': '', 'folder': foldername}
    json_string = json.dumps(moveJson) 
    moveresponse = requests.post(withdrawUrl, json_string)
    moveresponsejson = moveresponse.json()
    depositstatus = moveresponsejson['payload']['status']
    TASK_URL = baseUrl + 'tasks/' + moveresponsejson['payload']['id']
    while depositstatus == 'running':
        taskresponse = requests.get(TASK_URL)
        taskresponsejson = taskresponse.json()
        depositstatus = taskresponsejson['payload']['status']
        time.sleep(2)
        if(depositstatus == 'completed'):
            for filename in os.listdir(foldername):
                f = os.path.join(foldername, filename)
                if os.path.isfile(f):
                    print('FileName:',f)
                    with open(f, "rb") as fh:
                        fh = hikari.File(f)
                        await event.message.respond(fh)

            await event.message.respond('Coins Withdrawn')



