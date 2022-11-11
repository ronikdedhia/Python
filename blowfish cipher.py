from Crypto.Cipher import AES, ARC4, Blowfish, DES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
import time
import sys
stime = time.time()
plaintext = b'123456'
print(f'Plain text = {plaintext}')
blowfishInitVector = Random.new().read(Blowfish.block_size)
blowfish_key = b'Blowfishkey'
print(f'Key = {blowfish_key}')
blowfish_cipher = Blowfish.new(blowfish_key, Blowfish.MODE_CBC, blowfishInitVector)
blowfish_ciphertext = blowfish_cipher.encrypt(pad(plaintext, Blowfish.block_size))
print(f'Ciphertext = {blowfish_ciphertext}')
etime = time.time()
print(f'Encryption Time = {etime-stime}')
blowfish_cipher_decrypt = Blowfish.new(blowfish_key, Blowfish.MODE_CBC,
blowfishInitVector)
blowfish_plaintext_decrypt = unpad(blowfish_cipher_decrypt.decrypt(blowfish_ciphertext),
Blowfish.block_size)
print(f'Plaintext decrypted: {blowfish_plaintext_decrypt}')
print(f'Decryption Time = {time.time()-etime}')
print()
print('Avalanche effect 1 - Change in plaintext')
plaintext = b'122456'
print(f'Plain text = {plaintext}')
blowfishInitVector = Random.new().read(Blowfish.block_size)

blowfish_key = b'Blowfishkey'
print(f'Key = {blowfish_key}')
blowfish_cipher = Blowfish.new(blowfish_key, Blowfish.MODE_CBC, blowfishInitVector)
blowfish_ciphertext = blowfish_cipher.encrypt(pad(plaintext, Blowfish.block_size))
print(f'Ciphertext = {blowfish_ciphertext}')
blowfish_cipher_decrypt = Blowfish.new(blowfish_key, Blowfish.MODE_CBC,
blowfishInitVector)
blowfish_plaintext_decrypt = unpad(blowfish_cipher_decrypt.decrypt(blowfish_ciphertext),
Blowfish.block_size)
print(f'Plaintext decrypted: {blowfish_plaintext_decrypt}')
print()
print('Avalanche effect 2 - Change in key')
plaintext = b'123456'
print(f'Plain text = {plaintext}')
blowfishInitVector = Random.new().read(Blowfish.block_size)
blowfish_key = b'Blowdishkey'
print(f'Key = {blowfish_key}')
blowfish_cipher = Blowfish.new(blowfish_key, Blowfish.MODE_CBC, blowfishInitVector)
blowfish_ciphertext = blowfish_cipher.encrypt(pad(plaintext, Blowfish.block_size))
print(f'Ciphertext = {blowfish_ciphertext}')
blowfish_cipher_decrypt = Blowfish.new(blowfish_key, Blowfish.MODE_CBC,
blowfishInitVector)
blowfish_plaintext_decrypt = unpad(blowfish_cipher_decrypt.decrypt(blowfish_ciphertext),
Blowfish.block_size)
print(f'Plaintext decrypted: {blowfish_plaintext_decrypt}')