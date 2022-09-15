import hikari
import os
import lightbulb
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
from createnft import CreateNFT
from shownfts import ShowNFT
from withdrawnft import WithdrawNFT
bot = hikari.GatewayBot(token = os.environ['CCBOT_TOKEN'])

#https://patchwork.systems/programming/hikari-discord-bot/introduction-and-basic-bot.html
cmdbot = lightbulb.BotApp(token=os.environ['CCBOT_TOKEN'], prefix="myfix")
@cmdbot.command
# Use the command decorator to convert the function into a command
@lightbulb.option(
    "channel", "Channel to post announcement to.", type=str
)
@lightbulb.command("ping", "checks the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.Context when passed in
async def ping(ctx: lightbulb.Context,channel:str) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Ping-Pong!!!!-Got channel:"+ channel)

@cmdbot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("pong", "checks the bot is pong")

@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.Context when passed in
async def pong(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong-Ping!!!!")


cmdbot.run()
