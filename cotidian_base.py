# NFT contract: 0x2598ec45553d4f3D7aD8E78D0ECe6f299C407040 Base Sepolia, mainnet
# COTI testnet: 0x81b9adfa972281084ae49d707f0a4aa8af5c28f9

BOT_TOKEN = "<token goes here>"

import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View 
import urllib.parse

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Modal for sending ETH
class SendETHModal(discord.ui.Modal, title="Send ETH"):
    recipient = discord.ui.TextInput(
        label="Recipient Address",
        placeholder="Enter Ethereum address (e.g., 0x123...)",
        required=True
    )
    amount = discord.ui.TextInput(
        label="Amount (ETH)",
        placeholder="Enter amount (e.g., 0.1)",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        address = self.recipient.value
        amount = self.amount.value
        url = f"http://localhost:8000/Send.html?address={address}&amount={amount}"
        button = discord.ui.Button(label=f"Click to send {amount} ETH", style=discord.ButtonStyle.danger, url=url)
        view = View()
        view.add_item(button)
        await interaction.response.send_message(view=view, ephemeral=False)  

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message("An error occurred. Please try again.", ephemeral=True)

# Modal for minting NFT
class MintNFTModal(discord.ui.Modal, title="Mint NFT"):
    image = discord.ui.TextInput(
        label="URL",
        placeholder="Image link (e.g. IPFS)",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        img = self.image.value
        # URL-encode the values to handle special characters
        img_encoded = urllib.parse.quote(img)

        # Construct the URL with encoded values
        url = f"http://localhost:8000/MintNFT.html?image={img_encoded}"
        # await interaction.response.send_message(f"Click to mint NFT: {url}", ephemeral=True)
        button = discord.ui.Button(label=f"Click to mint NFT", style=discord.ButtonStyle.danger, url=url)
        view = View()
        view.add_item(button)
        await interaction.response.send_message(view=view, ephemeral=False)  

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message("An error occurred. Please try again.", ephemeral=True)

# Wallet command with enhanced embed and button UI
@bot.tree.command(name="wallet", description="Access wallet functionality")
async def wallet(interaction: discord.Interaction):
    # Create buttons with emojis
    send_eth_button = discord.ui.Button(label="💸 Send ETH", style=discord.ButtonStyle.primary, custom_id="send_eth")
    mint_nft_button = discord.ui.Button(label="🎨 Mint NFT", style=discord.ButtonStyle.success, custom_id="mint_nft")
    tbd_button = discord.ui.Button(label="💰 Become rich and attractive", style=discord.ButtonStyle.danger, custom_id="tbd")

    # Define button callbacks
    async def send_eth_callback(interaction: discord.Interaction):
        modal = SendETHModal()
        await interaction.response.send_modal(modal)

    async def mint_nft_callback(interaction: discord.Interaction):
        modal = MintNFTModal()
        await interaction.response.send_modal(modal)

    async def tbd_callback(interaction: discord.Interaction):
        await interaction.response.send_message("You are fine as you are. Learn to accept yourself.", ephemeral=True)

    send_eth_button.callback = send_eth_callback
    mint_nft_button.callback = mint_nft_callback
    tbd_button.callback = tbd_callback

    # Create view and add buttons
    view = discord.ui.View()
    view.add_item(send_eth_button)
    view.add_item(mint_nft_button)
    view.add_item(tbd_button)

    # Create embed
    embed = discord.Embed(
        title="",
        description="**Cotidian Wallet**\n\nYour non-custodial, trustless Discord interface for Web3  🌐",
        color=0x1E90FF  # DodgerBlue 
    )
    embed.add_field(name="This proof-of-concept is built on Base Network", value="", inline=True)
    embed.set_thumbnail(url="https://cdn-images-1.medium.com/v2/resize:fill:45:45/1*Xb63sEqj1pln3IhTTb2rSA.jpeg")  # Thumbnail
    embed.set_footer(text="👇 Click a button to get started")

    # Send the embed and view
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

bot.run(BOT_TOKEN)