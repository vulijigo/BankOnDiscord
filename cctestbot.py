import hikari
import os
from help import Help, ChooseHelp
bot = hikari.GatewayBot(token = os.environ['CCBOT_TOKEN'])

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.DMMessageCreateEvent)
async def ping(event: hikari.DMMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.

    command = event.content.split()
    if(command[0] == '/help'):
        if(len(command) == 1):
            helpContent = await Help()
            await event.message.respond(helpContent)
        else:
            helpContent = await ChooseHelp(command[1])
            await event.message.respond(helpContent)

    if len(event.message.attachments) > 0:
        print('attachments found')

    if event.is_bot or not event.content:
        return
    if event.content.startswith("ping"):
        await event.message.respond(str(event.author) + "-Pong!")
    print(event.channel_id)
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