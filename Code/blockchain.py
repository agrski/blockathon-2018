from datetime import datetime
import json

class BlockChain:

    def __init__(self, blockchain):
        self._blockchain = blockchain

    def add_block(self, block):
        if self.check_validity(block):
            self._blockchain.append(block)

    # Check that a blockchain is valid
    def check_validity(self, blockchain):
        pass

    def resolve_conflicting_blockchains(self, new_blockchain):
        # assume that registration document is a json string with key 'public_key'
        # step 0: compare which chain has most number of distinct public/private key pairs that signed the blocks.
        public_keys_A = set([json.loads(block.registration_document)['public_key'] for block in self._blockchain])
        public_keys_B = set([json.loads(block.registration_document)['public_key'] for block in new_blockchain.get_blockchain()])

        if len(public_keys_A) == len(public_keys_B):
            # step 1: if equal, select the greatest number of unique contributors from point of divergence
            divergence_index = self.find_divergence_index(new_blockchain)
            public_keys_A_from_divergence = public_keys_A[divergence_index:]
            public_keys_B_from_divergence = public_keys_B[divergence_index:]

            if len(public_keys_A_from_divergence) == len(public_keys_B_from_divergence):
                # step 2: if equal, select blockchain for which the private/public key pair (at point of divergence) signed the earliest block (before the point of divergence)
                predivergent_blocks = self._blockchain[:divergence_index]
                public_key_A = public_keys_A_from_divergence[0]
                public_key_B = public_keys_B_from_divergence[0]
                timestamps_A = [datetime.strptime(json.loads(block.registration_document)['timestamp'], '%Y/%m/%d') for block in predivergent_blocks if json.loads(block.registration_document)['public_key'] == public_key_A].sort()
                timestamps_B = [datetime.strptime(json.loads(block.registration_document)['timestamp'], '%Y/%m/%d') for block in predivergent_blocks if json.loads(block.registration_document)['public_key'] == public_key_B].sort()

                if timestamps_A[0] == timestamps_B[0]:
                    # step 3: if equal, select first public key from alphabetic order
                    if public_key_A < public_key_B:
                        return self._blockchain
                    else:
                        return new_blockchain

                elif timestamps_A[0] < timestamps_B[0]:
                    return self._blockchain
                else:
                    return new_blockchain

            elif len(public_keys_A_from_divergence) < len(public_keys_B_from_divergence):
                return new_blockchain
            else:
                return self._blockchain

        elif len(public_keys_A) < len(public_keys_B):
            return new_blockchain
        else:
            return self._blockchain

    def find_divergence_index(self, new_blockchain):
        pairs = zip(self._blockchain, new_blockchain)
        divergence_index = [json.loads(a.get_signature()) == json.loads(b.get_signature()) for a, b in pairs].index(False)
        return divergence_index

    def get_blockchain(self):
        return self._blockchain