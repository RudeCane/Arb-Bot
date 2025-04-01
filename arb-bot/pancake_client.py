from web3 import Web3
import os
import time
import json
from dotenv import load_dotenv

load_dotenv()

RPC = os.getenv("RPC_URL")
w3 = Web3(Web3.HTTPProvider(RPC))
router_address = Web3.to_checksum_address(os.getenv("PANCAKE_ROUTER"))
wallet_address = Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))
private_key = os.getenv("PRIVATE_KEY")

with import json

with open("router_abi.json", "r") as abi_file:
    router_abi = json.load(abi_file)


router = w3.eth.contract(address=router_address, abi=router_abi)

def get_pancake_price(token_address):
    token = Web3.to_checksum_address(token_address)
    path = [token, w3.to_checksum_address("0xe9e7cea3dedca5984780bafc599bd69add087d56")]  # TOKEN -> BUSD
    amounts = router.functions.getAmountsOut(Web3.to_wei(1, 'ether'), path).call()
    return Web3.from_wei(amounts[1], 'ether')

def buy_on_pancake(token_address, amount_wei):
    token = Web3.to_checksum_address(token_address)
    tx = router.functions.swapExactETHForTokens(
        0,
        [w3.to_checksum_address("0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"), token],
        wallet_address,
        int(time.time()) + 60
    ).build_transaction({
        'from': wallet_address,
        'value': amount_wei,
        'gas': 2000000,
        'gasPrice': w3.to_wei('5', 'gwei'),
        'nonce': w3.eth.get_transaction_count(wallet_address),
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()
