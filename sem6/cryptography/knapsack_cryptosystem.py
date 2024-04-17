import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    return pow(a, -1, m)

def generate_superincreasing_sequence(length):
    sequence = [random.randint(1, 10)]
    for _ in range(length - 1):
        sequence.append(random.randint(sum(sequence) + 1, 2 * sum(sequence)))
    return sequence

def generate_public_key(private_key):
    q = random.randint(sum(private_key) + 1, 2 * sum(private_key))
    r = random.randint(2, q - 1)
    public_key = [(r * k) % q for k in private_key]
    return public_key, q, r

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def encrypt(message, public_key):
    binary_message = text_to_binary(message)
    return sum(public_key[i] for i, bit in enumerate(binary_message) if bit == '1')

def decrypt(ciphertext, private_key, q, r):
    s = (ciphertext * mod_inverse(r, q)) % q
    plaintext = ""
    for i in range(len(private_key) - 1, -1, -1):
        if s >= private_key[i]:
            s -= private_key[i]
            plaintext = '1' + plaintext
        else:
            plaintext = '0' + plaintext
    return binary_to_text(plaintext)

def main():
    message = input("Enter the message to be encrypted: ")
    private_key = generate_superincreasing_sequence(len(message) * 8)  # Adjust for binary representation
    print("### Private Key ###\n", private_key)
    public_key, q, r = generate_public_key(private_key)
    print("\n### Public Key ###\n", public_key)
    encrypted_message = encrypt(message, public_key)
    print("\n### Encrypted Message ###\n", encrypted_message)
    decrypted_message = decrypt(encrypted_message, private_key, q, r)
    print("\n### Decrypted Message ###\n", decrypted_message)

if __name__ == "__main__":
    main()
