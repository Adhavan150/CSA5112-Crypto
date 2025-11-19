# Program 39: Frequency Attack Additive (Duplicate)
# Same as Program 15
def frequency_attack_additive():
    print("=== Frequency Attack on Additive Cipher ===")
    ciphertext = input("Enter ciphertext: ").upper()
    
    results = []
    for shift in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted += char
        results.append((shift, decrypted))
    
    num = int(input("Top N results (default 10): ") or "10")
    
    print(f"\nTop {num} possibilities:")
    for i in range(min(num, 26)):
        print(f"\n{i+1}. Shift {results[i][0]}:")
        print(results[i][1][:70])

if __name__ == "__main__":
    frequency_attack_additive()

OUTPUT:Enter ciphertext: PY
Top N results (default 10): 8
Top 8 possibilities:
1. Shift 0:
PY
2. Shift 1:
OX
3. Shift 2:
NW
4. Shift 3:
MV
5. Shift 4:
LU
6. Shift 5:
KT
7. Shift 6:
JS
8. Shift 7:
IR
