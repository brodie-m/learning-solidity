from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
from scripts.advanced.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    # arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for non-local")
    # act
    advanced_collectible, creating_tx = deploy_and_create()
    time.sleep(60)
    # assert
    assert advanced_collectible.tokenCounter() == 1
