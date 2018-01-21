import json
from pending_block import PendingBlock

from Crypto.Signature.PKCS1_v1_5 import PKCS115_SigScheme

class BlockChain:

    def __init__(self, blockchain):
        self._blockchain = blockchain

    def add_block(self, block):
        if self.check_new_block_validity():
            self._blockchain.append(block)

    def check_new_block_validity(self, block):
        if block.parent_signature == self._blockchain[-1].get_signature():
            public_keys = PendingBlock.encode_into_byte_string(block.parent_signature)
            for public_key in public_keys:
                encoded_registration_document = PendingBlock.encode_into_byte_string(block.registration_document)
                encoded_parent_signature = PendingBlock.encode_into_byte_string(block.parent_signature)
                hash_value = PendingBlock.hash_record_contents(encoded_registration_document, encoded_parent_signature)
                rsa_credentials = self.parse_public_key(public_key)
                sig_scheme = PKCS115_SigScheme(rsa_credentials)
                if not sig_scheme.verify(hash_value, block.get_signature()):
                    return False
            return True
        else:
            return False

    def check_block_validity(self, index):
        block = self._blockchain[index]
        parent_block = self.blockchain[index-1]
        if block.parent_signature == parent_block.get_signature():
            public_keys = PendingBlock.encode_into_byte_string(block.parent_signature)
            for public_key in public_keys:
                encoded_registration_document = PendingBlock.encode_into_byte_string(block.registration_document)
                encoded_parent_signature = PendingBlock.encode_into_byte_string(block.parent_signature)
                hash_value = PendingBlock.hash_record_contents(encoded_registration_document, encoded_parent_signature)
                rsa_credentials = self.parse_public_key(public_key)
                sig_scheme = PKCS115_SigScheme(rsa_credentials)
                if not sig_scheme.verify(hash_value, block.get_signature()):
                    return False
            return True
        else:
            return False

    def parse_public_key(self, public_key):
        pass

    # Check that a blockchain is valid
    def check_chain_validity(self):
        # check genesis block is valid
        genesis_block  = self._blockchain[0]
        if genesis_block.parent_signature == '' and genesis_block.registration_document == '' and genesis_block.get_signature() == ('', '', ''):
            validity_checks = [not(self.check_block_validity(self._blockchain.index(block))) for block in self._blockchain[1:]]
            return any(validity_checks)
        else:
            return False

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
                # step 2: if equal, select blockchain for which the private/public key pair (at point of divergence) signed the earliest block in the chian (index based)
                predivergent_blocks = self._blockchain[:divergence_index]
                public_key_A = public_keys_A_from_divergence[0]
                public_key_B = public_keys_B_from_divergence[0]
                indices_A = [predivergent_blocks.index(block) for block in predivergent_blocks if json.loads(block.registration_document)['public_key'] == public_key_A].sort()
                indices_B = [predivergent_blocks.index(block) for block in predivergent_blocks if json.loads(block.registration_document)['public_key'] == public_key_B].sort()

                if indices_A[-1] == indices_B[-1]:
                    # step 3: if equal, select first public key from alphabetic order
                    if public_key_A < public_key_B:
                        return self._blockchain
                    else:
                        return new_blockchain

                elif indices_A[-1] < indices_B[-1]:
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