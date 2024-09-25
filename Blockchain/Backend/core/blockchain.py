import sys
sys.path.append('/Users/Dell/OneDrive/Desktop/blockchain/bitcoin')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.core.util.util import hash256
from Blockchain.Backend.core.Database.database import BlockchainDB
import time


ZERO_HASH = '0' * 64
VERSION= 1

class Blockchain:
    def __init__(self):
        self.GenesisBlock()



    def write_on_disk(self, block):
        blockchaindb = BlockchainDB()
        blockchaindb.write(block)

    def fetch_last_block(self):
        blockchaindb = BlockchainDB()
        return blockchaindb.lastBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        PrevBlockHash = ZERO_HASH
        self.addblock(BlockHeight,PrevBlockHash)

    def addblock(self,BlockHeight, PrevBlockHash):
        timestamp = int(time.time())
        transaction = f"Codies Alert sent {BlockHeight} send to jeo"
        merkleRoot = hash256(transaction.encode()).hex()
        bits = "fFFf001f"
        blockheader = BlockHeader(VERSION,PrevBlockHash,merkleRoot,timestamp,bits) 
        blockheader.mine()
        self.write_on_disk([Block(BlockHeight,1,blockheader.__dict__,1,transaction).__dict__])

    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            blockHeight = lastBlock["Height"] + 1
            preBlockHash = lastBlock['BlockHeader']['blockhash']
            self.addblock(blockHeight,preBlockHash)


if __name__ == "__main__":

    blockchain = Blockchain()
    blockchain.main()  