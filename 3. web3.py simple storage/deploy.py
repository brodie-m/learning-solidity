import solcx
import json
import os
from web3 import Web3
from dotenv import load_dotenv

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
load_dotenv()

# compile solidity
solcx.install_solc("0.8.10")
compiled_sol = solcx.compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.10",
)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connect to ganache
w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/7aad57d9d94f4eb7ab6eead776b58916")
)
chain_id = 4
my_address = "0x5cF015757C88a2d8a4ee639faE1160a52bfd96d5"
private_key = os.getenv("PRIVATE_KEY")

# create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# get nonce from latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# build transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)

# sign transaction
signed_transaction = w3.eth.account.sign_transaction(
    transaction, private_key=private_key
)

# send tranasction
print("deploying contract...")
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("deployed!")
# working with the contract
# always need address and abi
simple_storage = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)

# initial val of favoriteNumber
print(simple_storage.functions.retrieve().call())
print("updating contract...")
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_txn = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
store_txn_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)
print("updated!")
print(simple_storage.functions.retrieve().call())
