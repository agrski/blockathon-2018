from Crypto.Hash.SHA256 import SHA256Hash
from Crypto.Signature.PKCS1_v1_5 import PKCS115_SigScheme

# pending block contents are:
# - parent signature
# - registration document (including public keys of signatories)
# - triple of signatures (first entry must be bureaucratic signature)


class PendingBlock:

    def __init__(self, rsa_key, registration_document, blockchain):
        self.registration_document = registration_document
        parent_signature = blockchain[-1].get_signature()
        encoded_registration_document = PendingBlock.encode_into_byte_string(registration_document)
        encoded_parent_signature = PendingBlock.encode_into_byte_string(parent_signature)
        hash_value = self.hash_record_contents(self, encoded_registration_document, encoded_parent_signature)
        self.signature = self.sign(rsa_key, hash_value)

    @classmethod
    def encode_into_byte_string(cls, message):
        return message.encode('utf-8', 'backslashreplace')

    @classmethod
    def hash_record_contents(cls, registration_document, parent_signature):
        hash_algorithm = SHA256Hash()
        hash_algorithm.update(registration_document+parent_signature)
        return hash.digest()

    @classmethod
    def sign(cls, rsa_key, hash_value):
        sig_scheme = PKCS115_SigScheme(rsa_key)
        signature = sig_scheme.sign(hash_value)
        return signature[0]

    def get_signature(self):
        return self._tribal_signature + self._bureaucratic_signature


# CONFLICT RESOLUTION

# find divergence point by overlapping coordinates.
# step 1: accept the block with the greatest number of unique public keys.
# step 2: accept the record whose public key added a record to the blockchain most recently since the point of divergence (check timetimestamp)



