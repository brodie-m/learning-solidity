from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import get_account, get_breed, OPENSEA_URL

dog_metadata = {
    "PUG": "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "ipfs://QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "ipfs://QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f'Working on {network.show_active()}')
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f'You have {number_of_collectibles} tokenIds')
    for token_id in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("ipfs://"):
            print(f'Setting tokenURI of {token_id}')
            set_tokenURI(token_id, advanced_collectible, dog_metadata[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f'Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address,token_id)}')
    print('Please wait up to 20 minutes and hit refresh metadata')
