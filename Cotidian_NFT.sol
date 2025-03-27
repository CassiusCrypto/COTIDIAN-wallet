// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.9.5/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.9.5/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract CotidianNFT is ERC721URIStorage {
    uint256 public tokenIdCounter;

    constructor() ERC721("CotidianNFT", "CNFT") {
        tokenIdCounter = 1; // Start at 1 for simplicity
    }

    function mint(address to, string memory tokenURI) public {
        uint256 newTokenId = tokenIdCounter;
        _safeMint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenIdCounter++;
    }
}