//SPDX-License-Identifier: MIT

pragma solidity 0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract DBrodToken is ERC20 {
    constructor() public ERC20("dBrod", "DBROD") {
        _mint(msg.sender, 1000000 * 1e18);
    }
}
