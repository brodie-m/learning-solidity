from brownie import BrodToken, accounts, network
from scripts.helpful_scripts import get_account


def main():
    get_reward()


def get_reward():
    account = get_account()
    brod_token = BrodToken[-1]
    tx = brod_token.giveMinerReward({"from": account})
    tx.wait(1)
    print(f'reward sent from {brod_token.address} to {account.address}')
