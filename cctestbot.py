import hikari
import os
from help import Help, ChooseHelp
from showcoins import ShowCoins
from deposit import Deposit
from statement import Statement
from pay import Pay
from move import Move
from withdraw import Withdraw
from deletewallet import DeleteWallet
from mywallet import MyWallet
from transfer import Transfer

#https://patchwork.systems/programming/hikari-discord-bot/introduction-and-basic-bot.html

bot = hikari.GatewayBot(token = os.environ['CCBOT_TOKEN'])

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.DMMessageCreateEvent)
async def ping(event: hikari.DMMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.

    if not event.content:
        return

    command = event.content.split()
    if(command[0] == '/bank'):
        walletName = str(event.author).replace("#","")
        if(len(command) > 1):
            phrase = command[1]
            if(phrase == 'deposit'):
                await Deposit(wallet= walletName, event=event)
            if(phrase == 'showcoins'):
                await ShowCoins(wallet= walletName, event=event)
            if(phrase == 'balance'):
                await ShowCoins(wallet= walletName, event=event)
            if(phrase == 'whatsmywallet'):
                await MyWallet(wallet= walletName, event=event)
            if(phrase == 'statement'):
                await Statement(wallet= walletName, event=event)
            if(phrase == 'deletewallet'):
                await DeleteWallet(wallet= walletName, event=event)
            if(phrase == 'withdraw'):
                amount = command[2]
                await Withdraw(wallet= walletName, event=event, amount= amount)
            if(phrase == 'transfer'):
                amount = command[2]
                skywallet = command[3]
                await Transfer(wallet= walletName, event=event, amount= amount, skywallet= skywallet)
            if(phrase == 'pay'):
                amount = command[2]
                print(walletName, amount)
                await Pay(wallet= walletName, event=event, amount=amount)
            if(phrase == 'move'):
                towallet = command[2]
                amount = command[3]
                await Move(wallet=walletName, event=event, towallet= towallet, amount= amount, type= 0)

    if(command[0] == '/help'):
        if(len(command) == 1):
            helpContent = await Help()
            await event.message.respond(helpContent)
        else:
            helpContent = await ChooseHelp(command[1])
            await event.message.respond(helpContent)

    if event.content.startswith("ping"):
        await event.message.respond(str(event.author) + "-Pong!")

@bot.listen(hikari.GuildMessageCreateEvent)
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    if event.content.startswith("ping"):
        await event.message.respond("Pong!")

bot.run()