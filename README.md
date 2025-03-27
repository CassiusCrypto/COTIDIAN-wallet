# COTIDIAN
COTIDIAN is a Discord-based interface for Web3 interactions.
COTIDIAN isn’t exactly a wallet, because it doesn’t store any funds or directly manage transactions. It uses MetaMask to confirm transactions, but makes it easy to interact with smart contracts by using a Discord bot. Discord itself doesn’t allow apps that popup MetaMask, for security reasons.

Find a runthrough at https://www.youtube.com/watch?v=5nockwjeuHU

Note that this does not require a hosted wallet (which would be a honeypot for hackers and would push a significant security burden onto the developer and Discord administrators), and no sensitive information is passed using the link. We’re just sending inputs to a smart contract and relying on MetaMask to deal with confirming the transaction itself. One of the benefits is that you can tailor and simplify the interaction, for example by providing some details for the transaction that the website would ask for. 

All of the steps involved – creating a Discord bot, writing the Discord app with Python, creating an html/JavaScript website to submit the transaction, and even writing and deploying the Solidity for the NFT smart contract to COTI testnet – were learned and completed using AI (mostly Grok).
