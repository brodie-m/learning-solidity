import React from 'react'
import { Token } from '../Main'
import { useEthers, useTokenBalance } from '@usedapp/core'
import { formatUnits } from 'ethers/lib/utils'
import BalanceMsg from '../BalanceMsg'
export interface WalletBalanceProps {
    token: Token
}
const WalletBalance = ({ token }: WalletBalanceProps) => {
    const { image, address, name } = token
    const { account } = useEthers()
    const tokenBalance = useTokenBalance(address, account)
    const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0

    return (
        <BalanceMsg
            label={`your un-staked ${name} balance`}
            tokenImgSrc={image}
            amount={formattedTokenBalance}
        />
    )
}

export default WalletBalance
