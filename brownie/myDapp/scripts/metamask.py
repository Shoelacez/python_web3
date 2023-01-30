import os
from brownie import accounts, Wei, web3
from dotenv import load_dotenv

load_dotenv()

def main():
    myWallet =  web3.eth.account.from_key(os.environ['pk'])
    walletAddress = myWallet.address
    walletBalance = web3.eth.getBalance(walletAddress) / 10**18
    print(f"Address: {walletAddress}")
    print(f"Balance: {walletBalance} ETH")
