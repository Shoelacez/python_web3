from django.shortcuts import render
from .models import Task

from web3 import Web3
from dotenv import load_dotenv
import os, json

load_dotenv()

# Create your views here.
def home(request):
    # Connect to the blockchain
    endpoint = "http://localhost:8545"
    web3_conn = Web3(Web3.HTTPProvider(endpoint))
    # Load the smart contract
    contract_address = os.environ["CONTRACT_ADDRESS"]
    contract_abi = json.loads(os.environ['ABI'])
    contract = web3_conn.eth.contract(address=contract_address, abi= contract_abi)
    # Query the state of the smart contract
    tasks = contract.functions.createTask("Task 01").call()
    task = {'name': tasks[1]}

    context = {"task": task}
    return render(request, "tasks/home.html", context)