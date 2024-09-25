from Blockchain.Backend.core.util.util import hash256

class BlockHeader:
    def __init__(self,version,prevBlockHash,MarkleRoot,Timestampm,Bits):
            self.version = version
            self.prevBlockHash = prevBlockHash
            self.MarkleRoot = MarkleRoot
            self.Timestampm = Timestampm
            self.Bits = Bits
            self.blockhash = ''
            self.nonce = 0

    def mine(self):
          while (self.blockhash[0:4]) != '0000':
                self.blockhash =  hash256((str(self.version)+ self.prevBlockHash + self.MarkleRoot+str(self.Timestampm)+str(self.nonce)).encode()).hex()
                self.nonce += 1
                print(f"mining started {self.nonce}", end ='\r')