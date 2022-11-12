from Crypto.Cipher import AES, ARC4, Blowfish, DES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random
import time
import sys
stime = time.time()
plaintext = b'123456'
print(f'Plain text = {plaintext}')
DESInitVector = Random.new().read(DES.block_size)
des_key = b'EightBit'
print(f'Key = {des_key}')
des_cipher = DES.new(des_key, DES.MODE_CBC, DESInitVector)
des_ciphertext = des_cipher.encrypt(pad(plaintext, DES.block_size))
print(f'Ciphertext: {des_ciphertext}')
etime = time.time()
print(f'Encryption Time = {etime - stime}')
cipher_des_decrypt = DES.new(des_key, DES.MODE_CBC, DESInitVector)
plaintext_decrypted_des = unpad(cipher_des_decrypt.decrypt(des_ciphertext), DES.block_size)
print(f'Decrypted Plaintext: {plaintext_decrypted_des}')
print(f'Decryption Time = {time.time() - etime}')
print()
print('Avalanche effect 1 - Change in plaintext')
plaintext = b'122456'
print(f'Plain text = {plaintext}')
DESInitVector = Random.new().read(DES.block_size)
des_key = b'EightBit'
print(f'Key = {des_key}')
des_cipher = DES.new(des_key, DES.MODE_CBC, DESInitVector)
des_ciphertext = des_cipher.encrypt(pad(plaintext, DES.block_size))
print(f'Ciphertext: {des_ciphertext}')
cipher_des_decrypt = DES.new(des_key, DES.MODE_CBC, DESInitVector)
plaintext_decrypted_des = unpad(cipher_des_decrypt.decrypt(des_ciphertext), DES.block_size)
print(f'Decrypted Plaintext: {plaintext_decrypted_des}')
print()
print('Avalanche effect 2 - Change in key')
plaintext = b'123456'
print(f'Plain text = {plaintext}')
DESInitVector = Random.new().read(DES.block_size)
des_key = b'EightBin'
print(f'Key = {des_key}')
des_cipher = DES.new(des_key, DES.MODE_CBC, DESInitVector)
des_ciphertext = des_cipher.encrypt(pad(plaintext, DES.block_size))
print(f'Ciphertext: {des_ciphertext}')
cipher_des_decrypt = DES.new(des_key, DES.MODE_CBC, DESInitVector)
plaintext_decrypted_des = unpad(cipher_des_decrypt.decrypt(des_ciphertext), DES.block_size)
print(f'Decrypted Plaintext: {plaintext_decrypted_des}')