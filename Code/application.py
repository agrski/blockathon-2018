# Author: Steven Ghoussain
# Date: Saturday 20th January 2018

from Crypto.PublicKey.RSA import RSA_Implementation
from pathlib import Path
import pickle

from pending_block import PendingBlock
from verified_block import VerifiedBlock
from blockchain import BlockChain
import config

# if rsa key does not already exist on file:
if not Path(config.key_file).is_file():
    # generate unique rsa key
    rsa = RSA_Implementation()
    rsa_key = rsa.generate(bits=384)
    # save to file
    with open(config.key_file, 'w') as f:
        pickle.dump(rsa_key, f)

# load rsa key
rsa_key = pickle.loads()

# hardcode genesis bloke
genesis = VerifiedBlock(registration_document='', tribal_signature_A='', tribal_signature_B='', bureaucratic_signature='')

# initialise blockchain
blockchain = BlockChain(genesis)

# initialise pending block queue
pending_block_queue = []


# api between local device and blockchain
# - submit a record for verification on the blockchain
def create_pending_block():
    # POST request
    # parse record from HTTP object
    record = 'something'
    pending_block = PendingBlock(rsa_key, record, blockchain)
    # add pending block to the queue
    pending_block_queue.append(pending_block)
    # send out the blockchain

# api to receive pending_blocks
# - add pending block to the queue
def receive_pending_block():
    # POST request
    # parse block from HTTP request body
    pass

