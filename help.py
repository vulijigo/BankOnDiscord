async def Help():
    depositContent = await DepositHelp()
    withdrawContent = await WithdrawHelp()
    mainContent = await MainHelp()
    moveContent = await moveHelp()
    payContent = await payHelp()
    balanceContent = await balanceHelp()
    statementContent = await statementHelp()
    return mainContent + depositContent + withdrawContent + moveContent + payContent + balanceContent + statementContent

async def MainHelp():
    return '**✳️ WELCOME TO CLOUDCOIN VAULT ✳️**\nThis bot allows you to deposit, withdraw and payout CloudCoins. This software is provided free of charge with all bugs, defects and vulnerabilities included free from the CloudCoin Consortium. \n\n**BASIC COMMANDS**'

async def MainNFTHelp():
    return '**✳️ WELCOME TO CLOUDCOIN NFT VAULT ✳️**\nThis bot allows you to create, list and withdraw NFTs powered by CloudCoin. This software is provided free of charge with all bugs, defects and vulnerabilities included free from the CloudCoin Consoritum. \n\n**BASIC COMMANDS ➡️**'

async def statementHelp():
    return '\n\n**🧾 STATEMENT**\n`/bank statement` Returns records of transactions\nNo extra information is required'

async def balanceHelp():
    return '\n\n**🔎 BALANCE**\n`/bank balance` Returns the number of coins in  your account\nNo extra information is required.'

async def payHelp():
    return "\n\n**❤️ PAY**\n`/bank pay` Places money from your account into the server's account and tells the server about the payment.\nRequires the number of coins to give the server: `/bank pay 50` where 50 is the number of coins to give the server/bot. "
    
async def moveHelp():
    return '\n\n**↔️ MOVE**\n`/bank move` Moves coins from your account to the account of another person\nRequires the number of coins to move and the user to move them to: `/bank move 10 larryG#3345` where 10 is the number of coins to move and larryG#3345 is the Discord user to receive the coins. They must have an account on this bot to receive coins. '

async def WithdrawHelp():
    return '\n\n**📤 WITHDRAW**\n`/bank withdraw` Removes cloudcoins from your account.\nRequires the amount of CloudCoins to be removed: `/bank withdraw 33` where 33 is the number of CloudCoins to be removed.'

async def DeleteWalletHelp():
    return '\n\n** 🚫 DELETE WALLET **\nDeletes the users wallet.\n\tRequest:\n /deletewallet\nReturns:\n\tWallet Deleted\nor\n\tYour Wallet Must Be Empty to be Deleted. Withdraw your Coins first.'

async def ShowCoinsHelp():
    return '\n\n** 👀 SHOWCOINS **\nShows all the coins that are in the users wallet. This number includes coins in the Bank folder and in the Fracked folder.\n\tRequest:\n `/showcoins`\nReturns an integer something like:\n\t33'

async def DepositHelp():
    return '\n\n** 📥 DEPOSIT**\n`/bank deposit` Creates and account if one does not exist. Uploads a CloudCoin file into your account\nFiles must have a .bin or .png file extension. Only CloudCoin 2.0 is supported. Type `/bank deposit` and then click the plus sign on the left to upload a file.  '

async def NFTCreateHelp():
    return '\n\n** 🎨 CREATE**\n`/nft create title description\nThis bot allows you to create NFTs from your cloudcoins in CloudBank. You must have a non zero balance in your wallet to create an NFT. This will create a new NFT wallet for you on the server.\n\n '
    
async def NFTsHOWHelp():
    return '\n\n**👀 SHOW**\n`/nft show Lists all the NFTs created by you in tabular format\n\n '
    
async def NFTWithdrawHelp():
    return '\n\n**📤 WITHDRAW**\n`/nft withdraw withdraws an NFT and sends back the PNG by discord bot\n\n '

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

async def NFTHelp():
        mainContent = await MainNFTHelp()
        nftCreateContent = await NFTCreateHelp()
        nftshowContent = await NFTsHOWHelp()
        nftWithdrawHelp = await NFTWithdrawHelp()
        return mainContent + nftCreateContent + nftshowContent + nftWithdrawHelp



