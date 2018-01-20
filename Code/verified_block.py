class VerifiedBlock:

    def __init__(self, registration_document, bureacratic_signature, tribal_signature_A, tribal_signature_B, blockchain):
        self.parent_signature = blockchain[-1].get_signature()
        self.registration_document = registration_document
        self._signature = (bureacratic_signature, tribal_signature_A, tribal_signature_B)

        def get_signature(self):
            return ''.join(self._signature)


# Block contents

# parent signature
# registration document:
# --- public key of signatories
# --- name of land owner
# --- GPS coordinates
# --- timestamp of sign-off
# triple of signatures