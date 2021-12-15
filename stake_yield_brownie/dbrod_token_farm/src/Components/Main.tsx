import React from 'react'
import { useEthers } from '@usedapp/core'
import helperConfig from '../helper-config.json'
import networkMap from '../chain-info/deployments/map.json'
import { constants } from 'ethers'
import brownieConfig from '../brownie-config.json'
import dBrod from '../dBrod.png'
import dai from '../dai.png'
import eth from '../eth.png'
import YourWallet from './YourWallet/YourWallet'
export type Token = {
    image: string,
    address: string,
    name: string
}
const Main = () => {
    const { chainId } = useEthers()
    const networkName = chainId ? helperConfig[chainId] : "dev"
    const dBrodTokenAddress = chainId ? networkMap[chainId]["DBrodToken"][0] : constants.AddressZero
    const wethTokenAddress = chainId ? brownieConfig["networks"][networkName]["weth_token"] : constants.AddressZero
    const fauTokenAddress = chainId ? brownieConfig["networks"][networkName]["fau_token"] : constants.AddressZero
    const supportedTokens: Array<Token> = [
        {
            image: dBrod,
            address: dBrodTokenAddress,
            name: "DBROD"
        },
        {
            image: dai,
            address: fauTokenAddress,
            name: "DAI"
        },
        {
            image: eth,
            address: wethTokenAddress,
            name: "WETH"
        }
    ]
    return (
        <YourWallet supportedTokens={supportedTokens} />
    )
}

export default Main
