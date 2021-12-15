import React from 'react'
import { useEthers } from '@usedapp/core'
import helperConfig from '../helper-config.json'
import networkMap from '../chain-info/deployments/map.json'
import { constants } from 'ethers'
import brownieConfig from '../brownie-config.json'
const Main = () => {
    const {chainId} = useEthers()
    const networkName = chainId ? helperConfig[chainId] : "dev"
    const dBrodTokenAddress = chainId ? networkMap[chainId]["DBrodToken"][0] : constants.AddressZero
    const wethTokenAddress = chainId ? brownieConfig["networks"][networkName]["weth_token"] : constants.AddressZero
    const fauTokenAddress = chainId ? brownieConfig["networks"][networkName]["fau_token"]: constants.AddressZero
    return (
        <div>
            
        </div>
    )
}

export default Main
