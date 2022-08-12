# BankOnDiscord
or 
# BankBot
Allows Companies to include CloudCoin Banks on their Discord Servers

This program is a Discord Bot that runs on a Discord Server. The idea is that many companies can  have their own Discord Banks. 

## BankBot Commands
To talk to the Bank Bot, the user types in "/bank". Then the user will be prompted for a command. Here are the commands available. All commands should be case insensitive including the parameters. 

1. [help](README.md#help)

2. [deletewallet](README.md#deletewallet)

3. [showcoins](README.md#showcoins)

4. [deposit](README.md#deposit)

5. [withdraw](README.md#withdraw)

6. [move](README.md#move)

7. [pay](README.md#pay)

8. [statement](README.md#statement)

9. [convert](README.md#convert)

10. We will be adding commands that support NFTs later including createNFT, deleteNFT, validateNFT etc.

## HELP
Returns a list off all the commands possible with explanations and uses

Sample Request completed at the Discord chat box. Note the use types in "/bank" then gets a prompt.
```
/bank help
```
Sample Response:
```
Commands available:
* help (returns commands and instructions)
* deletewallet (Deletes the user's wallet if it is empty. This is good for privacy reasons.)
...more commands
```


## DELETEWALLET
Deletes the users wallet. 

Request:
```
/bank deletewallet
```

Returns: 
```
Wallet Deleted
```
or 
```
Your Wallet Must Be Empty to be Deleted. Withdraw your Coins first.
```

## SHOWCOINS
Shows all the coins that are in the users wallet. This number includes coins in the Bank folder and in the Fracked folder. 

Request
```
/bank showcoins
```

Returns something like:
```
33
```

## DEPOSIT
This command will upload a coin file. I am not sure how the file will be uploaded. I assume the the file would be uploaded at the same time as the command is issued or it would be the next file. It could be that the user send the coin to the Bot and it is put into the users Import folder. Then the use issues the "deposit" command and all the files in the Import folder and imported. 
 Maybe the program will ask them to attach an image?

Request:
```
/bank deposit
```
Response:
```
Please attach an image with a .bin, .png or .stack extenstion that holds CloudCoins.
```
User then attaches a file. But, maybe they can attach a file with the first request and the stop above is not needed. 

The return will include the outcome and the receipt. Something like:
```
Coins Attempted: 1
Coins Authentic: 1

DETAILS: 
Receipt: 162e62e2484204d38cef95c8e5630ecf

08/12/2022 00:09

The Pownstring shows each of the 25s RAIDA’s responses from 0 to 24 encoded in a single character. p=pass, f=fail, u=untried, n=no response and e= error.

Serial Number : 9565182

Pownstring : ppppppppppppppppppppppppp

Result : Authentic
```
if something goes wrong it could return:
```
.stack files are legacy coins that can be converted at the rate of 85.125 to one. Please use the convert command instead. 
or
File was coorupted. Coins were not imported.
of
File extension not supported. Please upload .bin or .png files
```

## WITHDRAW
Brings the coin into the chat in the form of a PNG image and removes them from the wallet.

This command must specify the amount to with draw. Here is an example of the command to withdraw 20 coins:
```
/brank withdraw 30
```
A PNG will be returned. 

## MOVE
Moves coins from one person's wallet to another person's wallet. 
```
/bank move 25 jerry#34333
```
Response: 
```
25 moved to jerry#3433
```
or
```
Destination Wallet not found
```
Error: Destination wallet not found. The coins were not moved. 
```
## PAY
Gives the server owner CloudCoins and calls their hook. Their hook can look through the transaction log to verify payment.

Request to send the server owner 10 cloudcoins:
```
/bank pay 10
```
Response
```
Payment received. Your receipt number is 8787878782774344
```
or
```
Insufficient funds. Your balance is 3
```


## STATEMENT
Returns a history of transactions.

Request:
```
/bank statement
```

Response will look something  like:
```
8/12/22, 12:09 AM Deposit 1cc End Balance = 887
8/11/22, 7:35 PM Withdraw 1cc End Balance = 886
8/12/22, 12:09 AM  1cc End Balance = 887
```

## CONVERT
Converts legacy coins to CC2.0. The user's email is required. 

Request:
```
/bank convert Sean@myemail.com
```
Response: 
```
Please attach a .stack file
```

Return:
```
Returns errors associated with the convert and askse for their email.
```
or
```
Coins converted. Your new balance is 50
```


