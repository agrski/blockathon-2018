import Crypto.Hash.MD5 as MD5
import Crypto.PublicKey.RSA as RSA
import os

#takes the records to be in the block,
# the private key of the node creating the block and the current chain as inputs and returns the completed block
def make_block(records, chain, key, nodeID):
    parentBlock = chain[-1]
    parentSignature = parentBlock[u'signature']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    blockContents = {u'blockNumber': blockNumber, u'parentSignature':
        parentSignature, 'records': records
                     u'nodeID': nodeID}
    blockSignature = sign(blockContents, key)
    block = {u'signature': blockSignature, u'contents': blockContents}
    return block

#block is signed using the private key of the block creating node
def sign(blockContents, key, nodeID)
    # we created a hash to sign as this is more computationally efficient, but potentially less secure
    hash = MD5.new(blockContents).digest()
    # sign the hash
    signature = key.sign(hash, nodeID)
    return signature

#creates a new node, this function should only be called after the decision to create a new node has been approved and a node id selected
def create_node(nodeID)
    # Generates a fresh public/private key pair
    key[nodeID] = RSA.alg.generate(384, os.urandom)#384 is no. of bits that make up the key
    #can be altered to change security v compute time trade off
    pubkey[nodeID] = key[nodeID].publickey()
    return key[nodeID], pubkey[nodeID]

def check_block_hash(block, pubkey[nodeID])
    blockSignature = block[u'signature']
    blockcontent = block[u'contents']
    hash = MD5.new(blockcontent).digest()
    return pubkey[nodeID].verify(hash, blockSignature)

def get_node_id(block) # function to get node id from block
    return nodeID

#finds the point at which 2 chains diverge and calle this the
def find_divegent_point(chain1[], chain2[])
    return d

#given 2 chains it will pick the one that id prefered, chain's validity should be checked before this function is called
def pick_from_chains(chain1[], chain2[])
    for i in (1,len(chain1[])):
        nodeID[i] = get_node_id(chain1[i])
    countd1 = len(set(nodeID[]))
    for i in (1, len(chain2[])):
        nodeID[i] = get_node_id(chain2[i])
    countd2 = len(set(nodeID[]))
    if countd1 > countd2:
        return chain1[]
    elif countd2 > countd1:
        return chain2[]
    else:
        d = find_divegent_point(chain1[], chain2[])
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
            return chain1[]
        elif m > n:
            return chain2[]
        elif nodeID1 < nodeID2:
            return chain1[1]
        else nodeID2 =< nodeID1:
            return chain2[1]


