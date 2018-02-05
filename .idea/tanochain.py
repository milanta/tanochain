import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = str(index).encode()
        self.timestamp = str(timestamp).encode()
        self.data = data.encode()
        self.previous_hash = previous_hash.encode()
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(self.index)
        sha.update(self.timestamp)
        sha.update(self.data)
        sha.update(self.previous_hash)
        return sha.hexdigest()

def create_genesis_block():
        # Construimos un bloque manualmente con indice 0 y un hash anterior aleatorio.
        return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
        this_index = int(last_block.index) + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = last_block.hash
        return Block(int(this_index), this_timestamp, this_data, this_hash)


# Crea el Blockchain y agrega el bloque genesis.
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Cuantos bloques se agregaran a la cadena despues del bloque de genesis
num_of_blocks_to_add = 20

# Loop para agregar los bloques a la cadena
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print("Hash: {}\n".format(block_to_add.hash))
