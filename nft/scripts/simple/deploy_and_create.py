from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible

token_uri = "ipfs://QmXbVFrGMuA2x6qjvpaPuBmLSugT1BSUdAZCsdwphNYMtm"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}")
    return simple_collectible


def main():
    deploy_and_create()
