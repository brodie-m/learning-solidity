from os import link
from brownie import accounts, network, config, Contract
from web3 import Web3
import eth_utils

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat",
                                 "development", "ganache", "mainnet-fork"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


def encode_function_data(initializer=None, *args):
    if len(args) == 0 or not initializer:
        return eth_utils.to_bytes(hexstr="0x")
    return initializer.encode_input(*args)
