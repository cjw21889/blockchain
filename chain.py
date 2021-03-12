from block import Block
import json
from datetime import datetime

class BlockChain:
    def __init__(self):
        self.chain=[]
        self.transactions=[]
        self.genesis_block()

    def __str__(self):
        return str(self.__dict__)

    def genesis_block(self):
        genesis_block = Block('Genesis', 0x0,[3,4,5,6,7],datetime.now().timestamp(),0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block.hash)
        self.transactions.append(str(genesis_block.__dict__))
        return genesis_block

    def getLastBlock(self):
        return self.chain[-1]


    def proof_of_work(self, block):
        difficulty =1
        block.nonce=0
        computed_hash=block.compute_hash()
        while not (computed_hash.endswith('0' * difficulty) and ('55' * difficulty) in computed_hash):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add(self, data):
        block=Block(len(self.chain), self.chain[-1],data,datetime.now().timestamp(), 0)
        block.hash = self.proof_of_work(block)
        self.chain.append(block.hash)
        self.transactions.append(block.__dict__)
        return json.loads(str(block.__dict__).replace('\'', '\"'))

    def getTransactions(self, id):
        labels=['Manufacturer', 'Tansportation','Vendor']
        while True:
            try:
                if id =='all':
                    for i in range(len(self.transactions)-1):
                        print(f'{labels[i]}:\n{self.transactions[i+1]}\n')
                    break

                elif type(id)==int:
                    print(self.transactions[id])
                    break

            except Exception as e:
                print(e)




