import os
import requests
from pathlib import Path
PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
filepaths = [
    './img/pug.png',
    './img/shiba-inu.png',
    './img/st-bernard.png',
]
filenames = []
for filepath in filepaths:
    filenames.append(filepath.split("/")[-1:][0])
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY")
}


def main():
    for i in range(len(filepaths)):
        with Path(filepaths[i]).open("rb") as fp:
            image_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL+endpoint, files={"file": (filenames[i], image_binary)}, headers=headers)
            print(response.json())
