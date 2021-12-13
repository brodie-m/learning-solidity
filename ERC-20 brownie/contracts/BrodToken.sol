// contracts/BrodToken.sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract BrodToken is ERC20 {
    uint256 rewardAmount = 1000;

    constructor(uint256 initialSupply) ERC20("Brod", "BDM") {
        _mint(msg.sender, initialSupply);
    }

    function giveMinerReward() public {
        _mint(block.coinbase, rewardAmount);
    }
}
