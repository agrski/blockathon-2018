class BlockChain:

    def __init__(self, blockchain):
        self._blockchain = blockchain

    def add_block(self, block):
        if self.check_validity(block):
            self._blockchain.append(block)

    # Check that a blockchain is valid
    def check_validity(self, blockchain):
        pass

    def resolve_conflicting_blockchains(self, block_A, block_B):
        pass
        # step 0: compare which chain has most number of distinct public/private key pairs that signed the blocks.
        # step 1: if equal, select the greatest number of unique contributors from point of divergence
        # step 2: if equal, select whichever private/public key pair signed the earliest block (minimal index) (before the point of divergence)
        # step 3: first public key from alphabetic order

    def get_blockchain(self):
        return self._blockchain