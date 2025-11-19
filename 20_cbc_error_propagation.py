# Program 20: CBC Error Propagation
def cbc_error_propagation():
    print("=== CBC Mode Error Propagation ===")
    
    print("\nPart a) Error in transmitted ciphertext C1:")
    print("- P1 is completely corrupted (all bits affected)")
    print("- P2 has same bit error as C1 (1 bit affected)")
    print("- P3, P4, ... are NOT affected")
    print("Conclusion: Error affects only 2 blocks")
    
    print("\nPart b) Bit error in source plaintext P1:")
    print("At sender:")
    print("- C1 is affected (1 bit error)")
    print("- C2 is completely affected (avalanche effect)")
    print("- C3, C4, ... are NOT affected")
    
    print("\nAt receiver:")
    print("- P1 recovered correctly (1 bit error)")
    print("- P2 completely corrupted")
    print("- P3 onwards are correct")
    print("\nError propagates through 2 ciphertext blocks")

if __name__ == "__main__":
    cbc_error_propagation()

OUTPUT:Part a) Error in transmitted ciphertext C1:
- P1 is completely corrupted (all bits affected)
- P2 has same bit error as C1 (1 bit affected)
- P3, P4, ... are NOT affected
Conclusion: Error affects only 2 blocks

Part b) Bit error in source plaintext P1:
At sender:
- C1 is affected (1 bit error)
- C2 is completely affected (avalanche effect)
- C3, C4, ... are NOT affected

At receiver:
- P1 recovered correctly (1 bit error)
- P2 completely corrupted
- P3 onwards are correct

Error propagates through 2 ciphertext blocks
