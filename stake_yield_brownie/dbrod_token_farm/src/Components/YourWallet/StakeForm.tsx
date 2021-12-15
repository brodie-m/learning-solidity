import { formatUnits } from '@ethersproject/units'
import { Button, Input } from '@material-ui/core'
import { useEthers, useTokenBalance } from '@usedapp/core'
import React, { useState } from 'react'
import { Token } from '../Main'

export interface StakeFormProps {
    token: Token
}

const StakeForm = ({ token }: StakeFormProps) => {
    const [amount, setAmount] = useState<number | string | Array<number | string>>(0)
    const { address: tokenAddress, name } = token
    const { account } = useEthers()
    const tokenBalance = useTokenBalance(tokenAddress, account)
    const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0
    
    
    function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
        const newAmount = e.target.value === ""?"" : Number(e.target.value)
        setAmount(newAmount)
    }

    function handleClick(e: React.ChangeEvent) {

    }
    
    return (
        <>
            <Input onChange={handleChange}/>
            <Button color='secondary' variant='contained'>
                stake!
            </Button>
        </>
    )
}

export default StakeForm
