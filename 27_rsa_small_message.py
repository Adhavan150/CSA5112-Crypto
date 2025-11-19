# Program 27: RSA Small Message Attack
def rsa_small_message_attack():
    print("=== RSA Small Message Attack ===")
    
    print("\nScenario:")
    print("- Encrypting single characters (A-Z = 0-25)")
    print("- Each character encrypted separately")
    print("- Using RSA with large e and n")
    
    print("\nWhy this is INSECURE:")
    print("1. Only 26 possible plaintexts")
    print("2. Attacker can:")
    print("   - Encrypt all 26 letters")
    print("   - Build lookup table")
    print("   - Match ciphertext to plaintext")
    
    print("\nDemonstration:")
    e, n = 31, 3599
    print(f"\nPublic key: e={e}, n={n}")
    print("\nEncrypting A-Z:")
    
    for i in range(26):
        char = chr(65 + i)
        ciphertext = pow(i, e, n)
        print(f"{char} ({i:2d}) → {ciphertext:4d}")
    
    print("\nSolution: Use padding (OAEP)")
    print("- Adds randomness")
    print("- Makes plaintext large")
    print("- Prevents dictionary attacks")

if __name__ == "__main__":
    rsa_small_message_attack()

OUTPUT:Scenario:
- Encrypting single characters (A-Z = 0-25)
- Each character encrypted separately
- Using RSA with large e and n

Why this is INSECURE:
1. Only 26 possible plaintexts
2. Attacker can:
   - Encrypt all 26 letters
   - Build lookup table
   - Match ciphertext to plaintext

Demonstration:

Public key: e=31, n=3599

Encrypting A-Z:
A ( 0) →    0
B ( 1) →    1
C ( 2) → 3536
D ( 3) →  186
E ( 4) →  370
F ( 5) →  615
G ( 6) → 2678
H ( 7) → 1701
I ( 8) → 1883
J ( 9) → 2205
K (10) →  844
L (11) →  233
M (12) →  439
N (13) → 1660
O (14) →  807
P (15) → 2821
Q (16) →  138
R (17) → 2118
S (18) → 1446
T (19) → 3252
U (20) →  813
V (21) → 3273
W (22) → 3316
X (23) → 2539
Y (24) → 1135
Z (25) →  330
