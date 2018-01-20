import Crypto.Hash.MD5 as MD5
import Crypto.PublicKey.RSA as RSA
import os

def make_block(records, chain, key: int, nodeID: int):
    parentBlock = chain[-1]
    parentSignature = parentBlock['signature']
    blockNumber = parentBlock['contents']['blockNumber'] + 1
    blockContents = {'blockNumber': blockNumber,
                     'parentSignature': parentSignature,
                     'records': records,
                     'nodeID': nodeID,
                    }
    blockSignature = sign(blockContents, key)
    block = {'signature': blockSignature, 'contents': blockContents}
    return block

def sign(blockContents, key: int, nodeID: int)
    # Signing a hash is more computationally efficient
    hash = MD5.new(blockContents).digest()
    signature = key.sign(hash, nodeID)
    return signature

# This function should only be called after the decision to create a new node
# has been approved and a node id selected
def create_node(nodeID: int)
    # Generates a fresh public/private key pair
    key[nodeID] = RSA.alg.generate(384, os.urandom)
    pubkey[nodeID] = key[nodeID].publickey()
    return key[nodeID], pubkey[nodeID]

def check_block_hash(block, pubKey, nodeID)
    blockSignature = block['signature']
    blockcontent = block['contents']
    hash = MD5.new(blockcontent).digest()
    return pubKey[nodeID].verify(hash, blockSignature)

def get_node_id(block)
    return nodeID

def find_divegent_point(chain1: list, chain2: list)
    return d

# Chain validity should be checked before this function is called
def pick_from_chains(chain1: list, chain2: list)
    for i in (1,len(chain1)):
        nodeID[i] = get_node_id(chain1[i])
    countd1 = len(set(nodeID[]))
    for i in (1, len(chain2)):
        nodeID[i] = get_node_id(chain2[i])
    countd2 = len(set(nodeID[]))
    if countd1 > countd2:
        return chain1
    elif countd2 > countd1:
        return chain2
    else:
        d = find_divegent_point(chain1, chain2)
        nodeID1 = get_node_id(chain1[d+1])
        nodeID2 = get_node_id(chain2[d+1])
        n = 1
        while nodeID != nodeID1:
            nodeID = get_node_id(chain1[d-n])
            if nodeID == nodeID1:
                break
            n+=1
        m = 1
        while nodeID != nodeID2:
            nodeID = get_node_id(chain1[d-m])
            if nodeID == nodeID2:
                break
            m+=1
        if n > m:
            return chain1
        elif m > n:
            return chain2
        elif nodeID1 < nodeID2:
            return chain1[1]
        else nodeID2 =< nodeID1:
            return chain2[1]


