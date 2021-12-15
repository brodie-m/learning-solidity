import pytest
from scripts.helpful_scripts import get_account, get_contract, LOCAL_BLOCKCHAIN_ENVIRONMENTS, INITIAL_VALUE
from scripts.deploy import deploy_token_farm_and_dBrod_token
from brownie import network, config, exceptions


def test_set_pricefeed_contract():
    # arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing :)")
    account = get_account()
    non_owner = get_account(index=1)
    token_farm, dBrod_token = deploy_token_farm_and_dBrod_token()
    price_feed_address = get_contract("eth_usd_price_feed")
    # act
    token_farm.setPriceFeedContract(
        dBrod_token.address,
        price_feed_address,
        {"from": account})
    # assert
    assert token_farm.tokenPriceFeedMapping(
        dBrod_token.address) == price_feed_address
    with pytest.raises(exceptions.VirtualMachineError):
        token_farm.setPriceFeedContract(
            dBrod_token.address,
            price_feed_address,
            {"from": non_owner})


def test_stake_tokens(amount_staked):
    # arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing :)")
    account = get_account()
    token_farm, dBrod_token = deploy_token_farm_and_dBrod_token()
    # act
    dBrod_token.approve(token_farm.address, amount_staked, {"from": account})
    token_farm.stakeTokens(
        amount_staked,
        dBrod_token.address,
        {"from": account})
    # assert
    assert (
        token_farm.stakingBalance(
            dBrod_token.address, account.address) == amount_staked
    )
    assert token_farm.uniqueTokensStaked(account.address) == 1
    assert token_farm.stakers(0) == account.address
    return token_farm, dBrod_token


def test_issue_tokens(amount_staked):
    # arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing :)")
    account = get_account()
    non_owner = get_account(index=1)
    token_farm, dBrod_token = test_stake_tokens(amount_staked)
    starting_balance = dBrod_token.balanceOf(account.address)
    # act
    token_farm.issueTokens({"from": account})
    # assert
    assert (
        dBrod_token.balanceOf(
            account.address) == starting_balance + INITIAL_VALUE
    )
