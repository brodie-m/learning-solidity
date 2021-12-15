import pytest
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_token_farm_and_dBrod_token
from brownie import network, config


def test_set_pricefeed_contract():
    # arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing :)")
    account = get_account()
    non_owner = get_account(index=1)
    token_farm, dBrod_token = deploy_token_farm_and_dBrod_token()
