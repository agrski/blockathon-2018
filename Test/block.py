import sys
sys.path.append('../Code')
from blockchain import BlockChain
from Crypto.PublicKey.RSA import RSA_Implementation
from datetime import datetime
import time

genesis = [VerifiedBlock(registration_document='', tribal_signature_A='', tribal_signature_B='', bureaucratic_signature='')]

rsa = RSA_Implementation()
rsa_key = rsa.generate(bits=384)
public_key = [rsa_key]
ts = datetime.now()
ts = time.mktime(ts).timetuple()

chain = BlockChain(genesis)
blockchain.add_block(Block(public_key,
                           ts,
                           landowner='groundblocks',
                           coordinates=[(100000.00, 100000.00)],
                          )
                    )
