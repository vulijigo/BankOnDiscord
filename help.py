async def Help():
    return (await DeleteWalletHelp()) + '\n' (await ShowCoinsHelp()) + '\n' + (await DepositHelp())

async def DeleteWalletHelp():
    return 'Deletes the users wallet.\n\tRequest:\n /deletewallet\nReturns:\n\tWallet Deleted\nor\n\tYour Wallet Must Be Empty to be Deleted. Withdraw your Coins first.'

async def ShowCoinsHelp():
    return 'Shows all the coins that are in the users wallet. This number includes coins in the Bank folder and in the Fracked folder.\n\tRequest:\n /showcoins\nReturns an integer something like:\n\t33'

async def DepositHelp():
    return 'DEPOSIT\nThis command will upload a coin file. I am not sure how the file will be uploaded. I assume the the file would be uploaded at the same time as the command is issued or it would be the next file. It could be that the user send the coin to the Bot and it is put into the users Import folder. Then the use issues the "deposit" command and all the files in the Import folder and imported. Maybe the program will ask them to attach an image?\nRequest:\n\t/deposit\nResponse:\n\tPlease attach an image with a .bin, .png or .stack extenstion that holds CloudCoins.\nUser then attaches a file. But, maybe they can attach a file with the first request and the stop above is not needed.\nThe return will include the outcome and the receipt. Something like:\n\tCoins Attempted: 1\nCoins Authentic: 1\nDETAILS: \nReceipt: 162e62e2484204d38cef95c8e5630ecf\n08/12/2022 00:09\nThe Pownstring shows each of the 25s RAIDA’s responses from 0 to 24 encoded in a single character. p=pass, f=fail, u=untried, n=no response and e= error.\nSerial Number : 9565182\nPownstring : ppppppppppppppppppppppppp\nResult : Authentic\nif something goes wrong it could return:\n\t.stack files are legacy coins that can be converted at the rate of 85.125 to one. Please use the convert command instead. \nor\nFile was coorupted. Coins were not imported.\nor\nFile extension not supported. Please upload .bin or .png files'

async def ChooseHelp(help):
    if(help == 'deletewallet'):
        content = await DeleteWalletHelp()
        return content
    if(help == 'showcoins'):
        content = await ShowCoinsHelp()
        return content
    if(help == 'deposit'):
        content = await DepositHelp()
        return content

