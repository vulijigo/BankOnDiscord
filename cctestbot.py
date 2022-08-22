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
import tanjun

#https://patchwork.systems/programming/hikari-discord-bot/introduction-and-basic-bot.html

def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    client = (
        tanjun.Client.from_gateway_bot(
            bot,
            mention_prefix=True,
            declare_global_commands=1007899107320397886
        )
    ).add_prefix("!")
    client.load_modules("plugins.utilities")
    return client

bot = hikari.GatewayBot(token = os.environ['CCBOT_TOKEN'])
make_client(bot)

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
            if(phrase == 'statement'):
                await Statement(wallet= walletName, event=event)
            if(phrase == 'deletewallet'):
                await DeleteWallet(wallet= walletName, event=event)
            if(phrase == 'withdraw'):
                amount = command[2]
                await Withdraw(wallet= walletName, event=event, amount= amount)
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
            filename = 'test.txt'
            with open(filename, "rb") as fh:
                f = hikari.File(filename)
                await event.message.respond(f)
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