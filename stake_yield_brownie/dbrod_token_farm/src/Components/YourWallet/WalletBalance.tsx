import React from 'react'
import { Token } from '../Main'
import { useEthers, useTokenBalance } from '@usedapp/core'
import { formatUnits } from 'ethers/lib/utils'
export interface WalletBalanceProps {
    token: Token
}
const WalletBalance = ({ token }: WalletBalanceProps) => {
    const { image, address, name } = token
    const { account } = useEthers()
    const tokenBalance = useTokenBalance(address, account)
    const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0

    return (
        <div>
            {formattedTokenBalance}
        </div>
    )
}

export default WalletBalance
