class VerifiedBlock:

    def __init__(self, registration_document, bureacratic_signature, tribal_signature_A, tribal_signature_B):
        self.registration_document = registration_document
        self.bureacratic_signature = bureacratic_signature
        self.tribal_signature_A = tribal_signature_A
        self.tribal_signature_B = tribal_signature_B


# Block contents

# public key of signatories
# name of land owner
# GPS coordinates
# timestamp of sign-off
# (hash) tribal and bureaucratic signature