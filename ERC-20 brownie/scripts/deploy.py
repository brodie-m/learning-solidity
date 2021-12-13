from brownie import BrodToken, config, network
from scripts.helpful_scripts import get_account


def deploy_token():
    account = get_account()
    brod_token = BrodToken.deploy(
        1e6, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f'contract deployed to {brod_token.address}')


def main():
    deploy_token()
