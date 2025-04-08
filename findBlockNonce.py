def mine_block(k, prev_hash, transactions):
    """
    k - Number of trailing zeros in the binary representation (integer)
    prev_hash - the hash of the previous block (bytes)
    transactions - a list of "transactions," i.e., strings to be included in this block

    Find a nonce such that:
        sha256( prev_hash + transactions + nonce )
    has k trailing zeros in its *binary* representation
    """
    if not isinstance(k, int) or k < 0:
        print("mine_block expects positive integer")
        return b'\x00'

    # Convert the list of transaction strings to a single byte string
    tx_data = ''.join(transactions).encode('utf-8')

    nonce_int = 0
    while True:
        # Convert integer nonce to bytes
        nonce = str(nonce_int).encode('utf-8')

        # Concatenate prev_hash + tx_data + nonce
        block_data = prev_hash + tx_data + nonce

        # Hash the block
        block_hash = hashlib.sha256(block_data).digest()

        # Convert to binary representation
        hash_binary = bin(int.from_bytes(block_hash, byteorder='big'))

        # Check if the last k bits are zeros
        if hash_binary[-k:] == '0' * k:
            break

        nonce_int += 1

    assert isinstance(nonce, bytes), 'nonce should be of type bytes'
    return nonce
