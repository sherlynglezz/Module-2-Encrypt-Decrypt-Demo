# Module 2 Encrypt/Decrypt Demo

This Python program encrypts the message `Hello, Ivy Tech!` twice and decrypts both results to recover the original text. It prints the keys, original message, ciphertext, decrypted message, and whether the decrypted message matches the input. [demo_output.txt](demo_output.txt) contains a complete example run.

## Run the demo

Open a terminal in this folder. On Windows, run these commands.

```powershell
py -m pip install -r requirements.txt
py encryption_demo.py
```

To capture a new text file with your own run, use `py encryption_demo.py > demo_output.txt`.

## How the methods compare

| Method | How it works | Strength | Limitation |
| --- | --- | --- | --- |
| Symmetric (Fernet) | One secret key encrypts and decrypts. | Efficient for encrypting larger amounts of data. | Anyone who needs to decrypt must receive and protect the shared key. |
| Asymmetric (2048-bit RSA-OAEP with SHA-256) | The public key encrypts and the matching private key decrypts. | A sender can encrypt using the recipient's public key while the recipient keeps the private key. | Slower than symmetric encryption and limited to short inputs when used directly. |

The program encodes the message as UTF-8 bytes before encryption. It displays the RSA ciphertext as Base64 so the bytes can be read and copied as text. Both methods generate fresh keys each time the program runs, so the ciphertext changes while the recovered message stays the same.

The printed secret and private keys were generated solely for this classroom demo. Keep those keys private in real applications.
