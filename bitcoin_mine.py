import hashlib

# Simple demonstration of mining
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    nonce = 0
    while True:
        text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        if hash_result.startswith(prefix_str):
            print(f"Successfully mined block with nonce: {nonce}")
            return hash_result
        nonce += 1

# Parameters
block_number = 1
transactions = "TX1->TX2->TX3"
previous_hash = "00000000000000000000000000000000"
difficulty = 4

# Run the mining demonstration
mine(block_number, transactions, previous_hash, difficulty)