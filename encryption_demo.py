"""Demonstrate symmetric and asymmetric encryption of a short message."""

from base64 import b64encode

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def symmetric_demo(message):
    """Encrypt and decrypt with the same secret key."""
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)

    print("=== Symmetric encryption (Fernet) ===")
    print("Secret key:", key.decode("ascii"))
    print("Input:", message.decode("utf-8"))
    print("Encrypted output:", encrypted.decode("ascii"))
    print("Decrypted output:", decrypted.decode("utf-8"))
    print("Matches original:", decrypted == message)
    return decrypted


def asymmetric_demo(message):
    """Encrypt with the public key and decrypt with the private key."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    oaep = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
    encrypted = public_key.encrypt(message, oaep)
    decrypted = private_key.decrypt(encrypted, oaep)

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    print("\n=== Asymmetric encryption (RSA-OAEP with SHA-256) ===")
    print("Public key used to encrypt:\n" + public_pem.decode("ascii"), end="")
    print("Private key used to decrypt (demo only):\n" + private_pem.decode("ascii"), end="")
    print("Input:", message.decode("utf-8"))
    print("Encrypted output (Base64):", b64encode(encrypted).decode("ascii"))
    print("Decrypted output:", decrypted.decode("utf-8"))
    print("Matches original:", decrypted == message)
    return decrypted


def main():
    message = "Hello, Ivy Tech!".encode("utf-8")
    symmetric_demo(message)
    asymmetric_demo(message)


if __name__ == "__main__":
    main()
