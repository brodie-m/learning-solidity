from os import link
from brownie import accounts, network, config, LinkToken, VRFCoordinatorMock, Contract
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat",
                                 "development", "ganache", "mainnet-fork"]

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

contract_to_mock = {"link_token": LinkToken,
                    "vrf_coordinator": VRFCoordinatorMock}

BREED_MAPPING = {
    0: "PUG",
    1: "SHIBA_INU",
    2: "ST_BERNARD"
}


def get_breed(breed_number):
    return BREED_MAPPING[breed_number]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f'The active network is {network.show_active()}')
    print('deploying mocks...')
    account = get_account()
    print('deploy mock link token')
    link_token = LinkToken.deploy({"from": account})
    print(f'link token deployed to {link_token.address}')
    print('deploying mock vrf coordinator')
    vrf_coordinator = VRFCoordinatorMock.deploy(
        link_token.address, {"from": account})
    print(f'VRFCoordinator deployed to {vrf_coordinator.address}')
    print('all done')


def get_contract(contract_name):
    """ This function will grab the contract addresses from the brownie config
    if defined, otherwise it will deploy a mock version of that contract and
    return that mock contract.

        Args: 
            contract_name (string)
        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed
            version of this contract.

    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]

    else:
        contract_address = config["networks"][network.show_active(
        )][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi)

    return contract


def fund_with_link(
    contract_address,
    account=None,
    link_token=None,
    amount=Web3.toWei(1, 'ether')
):
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")
    funding_tx = link_token.transfer(
        contract_address, amount, {"from": account})
    funding_tx.wait(1)
    print(f'funded {contract_address}')
    return funding_tx
