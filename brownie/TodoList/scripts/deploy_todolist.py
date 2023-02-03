from brownie import Wei, accounts, ToDo, web3
import os, json
from dotenv import load_dotenv
from web3 import Web3


load_dotenv()

def main():
    deploy_account = web3.eth.account.from_key(os.environ['deploy_acc_pk'])
    
    deployment_details = {
        'from': deploy_account,
        'value': Wei('1 ether')
    }

    todo = ToDo.deploy(deployment_details)
    address = todo.address
    print(f"Address: {address}")

    # balance_todo = todo.balance()
    # print(f"Balance: {balance_todo}")

    # events_present = todo.events
    # print(f"Events: {events_present}")
