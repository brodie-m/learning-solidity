from scripts.helpful_scripts import get_account, get_contract
from brownie import DBrodToken, TokenFarm, config, network
from web3 import Web3
KEPT_BALANCE = Web3.toWei(100, 'ether')


def deploy_token_farm_and_dBrod_token():
    account = get_account()
    dBrod_token = DBrodToken.deploy(
        {"from": account}, publish_source=config["networks"][network.show_active()]["verify"])
    print('dBrod_token deployed')
    token_farm = TokenFarm.deploy(
        dBrod_token.address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"])
    print('token farm deployed')
    tx = dBrod_token.transfer(
        token_farm.address,
        dBrod_token.totalSupply() - KEPT_BALANCE,
        {"from": account})
    tx.wait(1)
    print("dBrod_token transferred")
    #dBrod_token, weth_token, fau_token(DAI)
    weth_token = get_contract("weth_token")
    fau_token = get_contract("fau_token")
    allowed_tokens = {
        dBrod_token: get_contract("dai_usd_price_feed"),
        fau_token: get_contract("dai_usd_price_feed"),
        weth_token: get_contract("eth_usd_price_feed"),
    }
    add_allowed_tokens(token_farm, allowed_tokens, account)
    return token_farm, dBrod_token


def add_allowed_tokens(token_farm, allowed_tokens, account):
    for token in allowed_tokens:
        add_tx = token_farm.addAllowedTokens(token.address, {"from": account})
        add_tx.wait(1)
        set_tx = token_farm.setPriceFeedContract(
            token.address, allowed_tokens[token], {"from": account})
        set_tx.wait(1)
    return token_farm


def main():
    deploy_token_farm_and_dBrod_token()
