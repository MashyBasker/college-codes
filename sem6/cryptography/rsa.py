import math
import random

def modular_inverse(a, m):
    return pow(a, -1, m)

def rsa_keygen(p: int, q: int):
    """
    Return an RSA key pair generated from the primes p and q.

    Preconditions:
    - p and q are primes
    - p != q
    """
    if p <= 2 or q <= 2:
        raise ValueError('p and q must be greater than 2')
    n = p * q # product of p and q
    phi_n = (p - 1) * (q - 1) 

    # choose e such that gcd(e, phi_n) = 1
    e = random.randint(2, phi_n-1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n-1)

    # choose d such that e * d % phi_n = 1
    d = modular_inverse(e,  phi_n)

    return ((p, q, d), (n, e))

def rsa_encrypt(pubk: tuple[int, int], plaintext: int):
    """
    Encrypt the plaintext with the received public key
    """
    n, e = pubk[0], pubk[1]
    encrypted = (plaintext ** e) % n
    return encrypted

def rsa_decrypt(privk: tuple[int, int, int], ciphertext: int):
    """
    Decrypt the ciphertext with the given private key
    """
    p, q, d = privk[0], privk[1], privk[2]
    n = p * q
    decrypted = (ciphertext ** d) % n
    return decrypted

def rsa_encrypt_text(pubkey: tuple[int, int], plaintext: str):
    """
    Encrypt a string using RSA with the public key
    """
    encrypted = ""
    for c in plaintext:
        encrypted += chr(rsa_encrypt(pubkey, ord(c)))
    return encrypted

def rsa_decrypt_text(privkey: tuple[int, int, int], ciphertext: str):
    """
    Decrypt a string using RSA with it's private key
    """
    decrypted = ""
    for c in ciphertext:
        decrypted += chr(rsa_decrypt(privkey, ord(c)))
    return decrypted

def main():
    # init
    p = 61
    q = 53
    
    # generate keys
    privkey, pubkey = rsa_keygen(p, q)
    print("Public key: ", pubkey)
    print("Private key: ", privkey)

    # encrypt the message
    plaintext = "I am vengeance!"
    print("Original message: ", plaintext)
    encrypted = rsa_encrypt_text(pubkey, plaintext)
    print("Encrypted message: ", encrypted)

    decrypted = rsa_decrypt_text(privkey, encrypted)
    print("Decrypted message: ", decrypted)

if __name__ == "__main__":
    main()

