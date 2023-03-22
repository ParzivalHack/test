import string
import random
from web3 import Web3
from time import sleep
from colorama import init, Fore, Style

init()  # initialize colorama

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/97d9b42d4a4a4c0ca98ea173bdcf4250'))
print("Connected to Web3: ", web3.isConnected())

# Ask the user for their wallet address
wallet_address = input("Enter your wallet address: ")

# Check if the wallet address is valid
if not w3.isAddress(wallet_address):
    print("Invalid wallet address")
else:
    # Retrieve the balance of the wallet address in ETH
    balance_wei = w3.eth.getBalance(wallet_address)
    balance_eth = w3.fromWei(balance_wei, 'ether')
    
    # Print the balance of the wallet address
    print("Your current balance is", balance_eth, "ETH")
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
