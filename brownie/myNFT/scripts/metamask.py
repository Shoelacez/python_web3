from brownie import web3, Wei,accounts,WiccaToken
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    myWallet = web3.eth.account.from_key(os.environ['pk'])
    balance = web3.eth.getBalance(myWallet.address) / 10**18
    print(f"Metamask Balance: {balance} ETH")

    print(f"Metamask Address: {myWallet.address}")