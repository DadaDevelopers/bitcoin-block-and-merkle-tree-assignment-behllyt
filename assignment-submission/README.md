# Bitcoin Block and Merkle Tree Assignment

## Overview
This assignment explores Bitcoin block structure and Merkle tree
construction through hands-on inspection and code implementation.

## Files
- block-inspection.md - Task 1 block inspection results
- code/merkle_tree.py - Task 2 Merkle tree implementation
- output.txt - Output from running merkle_tree.py
- README.md - This file

## How to Run
python3 code/merkle_tree.py

## Task 1 Summary
Inspected Bitcoin block 888888 using mempool.space.
Documented block hash, previous block hash, merkle root,
number of transactions and timestamp.

## Task 2 Summary
Built a Merkle tree from 4 transaction hashes:
- TxA, TxB, TxC, TxD are the leaf nodes
- Hash(AB) = double_sha256(TxA + TxB)
- Hash(CD) = double_sha256(TxC + TxD)
- Merkle Root = double_sha256(Hash(AB) + Hash(CD))

Final Merkle Root:
a157aa34442f29fcb1d945b4309d8954ebae056427b5934f01745731921a7cb1

## Key Learnings
1. Every block contains a merkle root that summarizes all transactions
2. Changing any transaction changes the merkle root
3. Blocks are linked via previous block hash forming a chain
4. Merkle trees allow efficient proof of transaction inclusion
5. Double SHA256 is used for all Bitcoin hashing operations
