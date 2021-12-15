import { formatUnits } from '@ethersproject/units'
import { Button, Input } from '@material-ui/core'
import { useEthers, useTokenBalance } from '@usedapp/core'
import React from 'react'
import { Token } from '../Main'

export interface StakeFormProps {
    token: Token
}

const StakeForm = ({ token }: StakeFormProps) => {
    const { address: tokenAddress, name } = token
    const { account } = useEthers()
    const tokenBalance = useTokenBalance(tokenAddress, account)
    const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0
    return (
        <>
            <Input />
            <Button color='secondary' variant='contained'>
                stake!
            </Button>
        </>
    )
}

export default StakeForm
