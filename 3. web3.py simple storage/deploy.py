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
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xBcE6fb9D36B6f4c9d0e72fe4ff98a97b757C1AE5"
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
print(signed_transaction)
# send tranasction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
