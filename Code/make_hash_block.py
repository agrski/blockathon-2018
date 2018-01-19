#takes the records to be in the block,
# the private key of the node creating the block and the current chain as inputs and returns the completed block
def make_block(records, chain, key, nodeid):
    parentBlock = chain[-1]
    parentsignature = parentBlock[u'signature']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    blockContents = {u'blockNumber': blockNumber, u'parentsignature':
        parentsignature, 'records': records
                     u'nodeid': nodeid}
    blocksignature = sign(blockContents, key)
    block = {u'signature': blocksignature, u'contents': blockContents}
    return block

#block is signed using the private key of the block creating node
def sign(blockContents, key, nodeid)
    import Crypto.Hash.MD5 as MD5
    # we created a hash to sign as this is more computationally efficient, but potentially less secure
    hash = MD5.new(blockContents).digest()
    # sign the hash
    signature = key.sign(hash, nodeid)
    return signature

#creates a new node, this function should only be called after the decision to create a new node has been approved and a node id selected
def create_node(nodeid)
    import Crypto.PublicKey.RSA as RSA
    import os
    # Generates a fresh public/private key pair
    key[nodeid] = RSA.alg.generate(384, os.urandom)#384 is no. of bits that make up the key
    #can be altered to change security v compute time trade off
    pubkey[nodeid] = key[nodeid].publickey()
    return key[nodeid], pubkey[nodeid]

def check_block_hash(block, pubkey[nodeid])
    blocksignature = block[u'signature']
    blockcontent = block[u'contents']
    hash = MD5.new(blockcontent).digest()
    return pubkey[nodeid].verify(hash, blocksignature)

def get_node_id(block) # function to get node id from block
    return nodeid

#finds the point at which 2 chains diverge and calle this the
def find_divegent_point(chain1[], chain2[])
    return d

#given 2 chains it will pick the one that id prefered, chain's validity should be checked before this function is called
def pick_from_chains(chain1[], chain2[])
    for i in (1,len(chain1[])):
        nodeid[i] = get_node_id(chain1[i])
    countd1 = len(set(nodeid[]))
    for i in (1, len(chain2[])):
        nodeid[i] = get_node_id(chain2[i])
    countd2 = len(set(nodeid[]))
    if countd1 > countd2:
        return chain1[]
    elif countd2 > countd1:
        return chain2[]
    else:
        d = find_divegent_point(chain1[], chain2[])
        nodeid1 = get_node_id(chain1[d+1])
        nodeid2 = get_node_id(chain2[d+1])
        n = 1
        while nodeid != nodeid1:
            nodeid = get_node_id(chain1[d-n])
            if nodeid == nodeid1:
                break
            n+=1
        m = 1
        while nodeid != nodeid2:
            nodeid = get_node_id(chain1[d-m])
            if nodeid == nodeid2:
                break
            m+=1
        if n > m:
            return chain1[]
        elif m > n:
            return chain2[]
        elif nodeid1 < nodeid2:
            return chain1[1]
        else nodeid2 =< nodeid1:
            return chain2[1]


