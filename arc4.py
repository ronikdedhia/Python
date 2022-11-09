from Crypto.Cipher import AES, ARC4, Blowfish, DES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
import time
import sys
stime = time.time()
plaintext = b'123456'
print(f'Plain text = {plaintext}')
ARC4_key = b'ThisIsRC4Key'
print(f'Key = {ARC4_key}')
ARC4_cipher = ARC4.new(ARC4_key)
ARC4_ciphertext = ARC4_cipher.encrypt(plaintext)
print(f'Ciphertext = {ARC4_ciphertext}')
etime = time.time()
print(f'Encryption Time = {etime-stime}')
ARC4_cipher_decrypt = ARC4.new(ARC4_key)
ARC4_plaintext_decrypted = ARC4_cipher_decrypt.decrypt(ARC4_ciphertext)
print(f'Decrypted Plaintext = {ARC4_plaintext_decrypted}')
print(f'Decryption Time = {time.time() - etime}')
print()
print('Avalanche Effect 1 - Change in plaintext')
plaintext = b'122456'
print(f'Plain text = {plaintext}')
ARC4_key = b'ThisIsRC4Key'
print(f'Key = {ARC4_key}')
ARC4_cipher = ARC4.new(ARC4_key)
ARC4_ciphertext = ARC4_cipher.encrypt(plaintext)
print(f'Ciphertext = {ARC4_ciphertext}')
ARC4_cipher_decrypt = ARC4.new(ARC4_key)
ARC4_plaintext_decrypted = ARC4_cipher_decrypt.decrypt(ARC4_ciphertext)
print(f'Decrypted Plaintext = {ARC4_plaintext_decrypted}')
print()
print('Avalanche Effect 2 - Change in key')
plaintext = b'123456'
print(f'Plain text = {plaintext}')
ARC4_key = b'ThisIsRC3Key'
print(f'Key = {ARC4_key}')
ARC4_cipher = ARC4.new(ARC4_key)
ARC4_ciphertext = ARC4_cipher.encrypt(plaintext)
print(f'Ciphertext = {ARC4_ciphertext}')
ARC4_cipher_decrypt = ARC4.new(ARC4_key)
ARC4_plaintext_decrypted = ARC4_cipher_decrypt.decrypt(ARC4_ciphertext)
print(f'Decrypted Plaintext = {ARC4_plaintext_decrypted}')
