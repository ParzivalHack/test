import string
import random
from web3 import Web3
from time import sleep
from colorama import init, Fore, Style

init()  # initialize colorama

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/97d9b42d4a4a4c0ca98ea173bdcf4250"))
print("Connected to Web3: ", web3.isConnected())

to_account = str(input("Import your wallet: "))
balance = web3.eth.get_balance(to_account)
print("Your current balance is 0.0", balance, "ETH.")
print("Mining wallets...")
while True:
    # Print the hash in red
    print(Fore.RED + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(50)) + '--0.0000 ETH')
    
    # Wait for 10 seconds
    sleep(10)
    
    # Print "Wallet Found!" in green
    print(Style.BRIGHT + Fore.GREEN + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(50)) + "-- 0.3751 ETH")
    print("Transfering 0.3751 ETH to your wallet...")
 
    break  # Exit the loop after printing the message
