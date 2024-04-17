import unittest
from rsa import rsa_keygen, rsa_encrypt_text, rsa_decrypt_text

class TestRSA(unittest.TestCase):
    def test_rsa_encrypt_decrypt(self):
        # Test with different plaintexts
        plaintexts = ["Hello, RSA!", "This is a test message.", "1234567890"]
        p = 61
        q = 53
        private_key, public_key = rsa_keygen(p, q)

        for plaintext in plaintexts:
            # Encrypt the message
            encrypted_text = rsa_encrypt_text(public_key, plaintext)
            print(f"Plaintext: {plaintext}, Encrypted Text: {encrypted_text}")

            # Decrypt the message
            decrypted_text = rsa_decrypt_text(private_key, encrypted_text)
            print(f"Decrypted Text: {decrypted_text}")
            print("\n")
            # Check if decrypted message matches original plaintext
            self.assertEqual(plaintext, decrypted_text)

    def test_rsa_keygen(self):
        # Test key generation with small primes
        p = 17
        q = 19
        private_key, public_key = rsa_keygen(p, q)

        self.assertIsInstance(public_key, tuple)
        self.assertIsInstance(private_key, tuple)

    def test_rsa_encrypt_decrypt_edge_cases(self):
        # Test edge cases with empty plaintext
        p = 61
        q = 53
        private_key, public_key = rsa_keygen(p, q)

        plaintext = ""
        encrypted_text = rsa_encrypt_text(public_key, plaintext)
        print(f"Plaintext: {plaintext}, Encrypted Text: {encrypted_text}")

        decrypted_text = rsa_decrypt_text(private_key, encrypted_text)
        print(f"Decrypted Text: {decrypted_text}")
        print("\n")
        self.assertEqual(plaintext, decrypted_text)

        # Test edge cases with small prime numbers
        p = 11
        q = 31
        private_key, public_key = rsa_keygen(p, q)

        plaintext = "A"
        encrypted_text = rsa_encrypt_text(public_key, plaintext)
        print(f"Plaintext: {plaintext}, Encrypted Text: {encrypted_text}")

        decrypted_text = rsa_decrypt_text(private_key, encrypted_text)
        print(f"Decrypted Text: {decrypted_text}")
    
        self.assertEqual(plaintext, decrypted_text)

if __name__ == "__main__":
    unittest.main()
