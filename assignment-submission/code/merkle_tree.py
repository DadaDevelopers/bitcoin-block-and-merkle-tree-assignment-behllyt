import hashlib

def double_sha256(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def calculate_merkle_tree(txids):
    print("=== Merkle Tree Construction ===")
    print("")
    print("Input Transactions:")
    for i, txid in enumerate(txids):
        print("  TxA B C D"[i*2] + ": " + txid)
    print("")

    # Convert to bytes
    hashes = [bytes.fromhex(txid)[::-1] for txid in txids]

    # Level 0 - leaf nodes
    print("Level 0 - Leaf Nodes (Transactions):")
    labels = ["TxA", "TxB", "TxC", "TxD"]
    for i, h in enumerate(hashes):
        print("  " + labels[i] + ": " + h[::-1].hex())
    print("")

    # Level 1 - combine pairs
    print("Level 1 - Combining Pairs:")
    level1 = []
    for i in range(0, len(hashes), 2):
        combined = hashes[i] + hashes[i+1]
        result = double_sha256(combined)
        level1.append(result)
        if i == 0:
            label = "Hash(AB)"
        else:
            label = "Hash(CD)"
        print("  " + label + ": " + result[::-1].hex())
    print("")

    # Level 2 - merkle root
    print("Level 2 - Merkle Root:")
    combined = level1[0] + level1[1]
    merkle_root = double_sha256(combined)[::-1].hex()
    print("  MerkleRoot: " + merkle_root)
    print("")

    return merkle_root

def print_diagram(txids, level1_hashes, merkle_root):
    print("=== Merkle Tree Diagram ===")
    print("")
    print("                    " + merkle_root[:8] + "... (Merkle Root)")
    print("                        |")
    print("            +-----------+-----------+")
    print("            |                       |")
    print("  " + level1_hashes[0][:8] + "... (Hash AB)    " + level1_hashes[1][:8] + "... (Hash CD)")
    print("            |                       |")
    print("        +---+---+               +---+---+")
    print("        |       |               |       |")
    print("  " + txids[0][:8] + "...  " + txids[1][:8] + "...  " + txids[2][:8] + "...  " + txids[3][:8] + "...")
    print("   (TxA)    (TxB)      (TxC)    (TxD)")
    print("")

if __name__ == "__main__":
    # 4 example transaction hashes
    txids = [
        "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
        "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
        "c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4",
        "d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5"
    ]

    # Calculate level 1 hashes for diagram
    hashes = [bytes.fromhex(txid)[::-1] for txid in txids]
    level1 = []
    for i in range(0, len(hashes), 2):
        combined = hashes[i] + hashes[i+1]
        result = double_sha256(combined)
        level1.append(result[::-1].hex())

    merkle_root = calculate_merkle_tree(txids)
    print_diagram(txids, level1, merkle_root)

    print("=== Summary ===")
    print("Step 1: Start with 4 transaction hashes as leaf nodes")
    print("Step 2: Hash TxA + TxB together to get Hash(AB)")
    print("Step 3: Hash TxC + TxD together to get Hash(CD)")
    print("Step 4: Hash Hash(AB) + Hash(CD) to get Merkle Root")
    print("Final Merkle Root: " + merkle_root)
