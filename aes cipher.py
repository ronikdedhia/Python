from Crypto.Cipher import AES, ARC4, Blowfish, DES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
import time
import sys
stime = time.time()
plaintext = b'123456'
print(f'Plain text = {plaintext}')
initVector = Random.new().read(AES.block_size)
#print(initVector)
aes_key = b'MySecretPassword'
print(f'Key = {aes_key}')
aes_cipher = AES.new(aes_key, AES.MODE_CBC, initVector)
ciphertext = aes_cipher.encrypt(pad(plaintext, AES.block_size))
print(f'Ciphertext = {ciphertext}')
etime = time.time()
print(f'Encryption Time = {etime - stime}')
#print(sys.getsizeof(ciphertext))
cipher_aes_decrypt = AES.new(aes_key, AES.MODE_CBC, initVector)
plaintext_decrypted = unpad(cipher_aes_decrypt.decrypt(ciphertext), AES.block_size)
print(f'Decrypted Text = {plaintext_decrypted}')
print(f'Decryption Time = {time.time()-etime}')
print()
print("Avalanche effect 1 - Change in plaintext ")
plaintext = b'122456'
print(f'Plain text = {plaintext}')
initVector = Random.new().read(AES.block_size)
#print(initVector)
aes_key = b'MySecretPassword'
print(f'Key = {aes_key}')
aes_cipher = AES.new(aes_key, AES.MODE_CBC, initVector)
ciphertext = aes_cipher.encrypt(pad(plaintext, AES.block_size))
print(f'Ciphertext = {ciphertext}')
#print(sys.getsizeof(ciphertext))
cipher_aes_decrypt = AES.new(aes_key, AES.MODE_CBC, initVector)
plaintext_decrypted = unpad(cipher_aes_decrypt.decrypt(ciphertext), AES.block_size)
print(f'Decrypted Text = {plaintext_decrypted}')
print()
print("Avalanche effect 2 - Change in key ")
plaintext = b'123456'
print(f'Plain text = {plaintext}')
initVector = Random.new().read(AES.block_size)
#print(initVector)
aes_key = b'MySecretPasswotd'
print(f'Key = {aes_key}')
aes_cipher = AES.new(aes_key, AES.MODE_CBC, initVector)
ciphertext = aes_cipher.encrypt(pad(plaintext, AES.block_size))
print(f'Ciphertext = {ciphertext}')
#print(sys.getsizeof(ciphertext))
cipher_aes_decrypt = AES.new(aes_key, AES.MODE_CBC, initVector)
plaintext_decrypted = unpad(cipher_aes_decrypt.decrypt(ciphertext), AES.block_size)
print(f'Decrypted Text = {plaintext_decrypted}')