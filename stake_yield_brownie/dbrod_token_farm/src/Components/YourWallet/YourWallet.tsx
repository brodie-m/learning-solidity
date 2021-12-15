import { Box, Tab } from '@material-ui/core'
import React, { useState } from 'react'
import { Token } from '../Main'
import { TabContext, TabList, TabPanel } from '@material-ui/lab'
import WalletBalance from './WalletBalance'
import StakeForm from './StakeForm'
interface YourWalletProps {
    supportedTokens: Array<Token>
}

const YourWallet = ({ supportedTokens }: YourWalletProps) => {

    const [selectedTokenIndex, setSelectedTokenIndex] = useState<number>(0)

    function handleChange(e: React.ChangeEvent<{}>, newValue: string) {

        setSelectedTokenIndex(parseInt(newValue))
    }

    return (
        <Box>
            <h1>your wallet</h1>
            <Box>
                <TabContext value={selectedTokenIndex.toString()}>
                    <TabList onChange={handleChange} aria-label="stake form tabs">
                        {supportedTokens.map((tok, idx) => {
                            return (
                                <Tab
                                    label={tok.name}
                                    key={idx}
                                    value={idx.toString()}
                                />
                            )
                        })}
                    </TabList>
                    {supportedTokens.map((t, i) => {
                        return (

                            <TabPanel value={i.toString()} key={i}>
                                <div>
                                    <WalletBalance token={supportedTokens[i]} />
                                    <StakeForm token={supportedTokens[i]} />
                                </div>
                            </TabPanel>
                        )
                    })}
                </TabContext>
            </Box>
        </Box>
    )
}

export default YourWallet
