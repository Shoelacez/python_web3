// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

contract Counter{
    uint public count;

    function inc() public returns(uint updated_count){
        count += 1;
        updated_count = count;
    }

    function dec() public returns (uint){
        count -= 1;
        return count;
    }
}