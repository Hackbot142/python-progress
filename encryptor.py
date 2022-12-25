import base64
from Crypto.Cipher import AES

def encrypt(key, plaintext):
  key = key.encode()
  plaintext = plaintext.encode()
  
  pad = 16 - (len(plaintext) % 16)
  plaintext = plaintext + pad * chr(pad).encode()
  
  cipher = AES.new(key, AES.MODE_EAX)
  ciphertext, tag = cipher.encrypt_and_digest(plaintext)
  
  ciphertext = base64.b64encode(ciphertext).decode()
  tag = base64.b64encode(tag).decode()
  
  return (ciphertext, tag)

def decrypt(key, ciphertext, tag):
  key = key.encode()
  ciphertext = base64.b64decode(ciphertext.encode())
  tag = base64.b64decode(tag.encode())
  
  cipher = AES.new(key, AES.MODE_EAX, tag)
  plaintext = cipher.decrypt(ciphertext)
  
  pad = plaintext[-1]
  plaintext = plaintext[:-pad]
  
  return plaintext.decode()

key = 'secretkey12345678'
plaintext = 'Hello, world!'
ciphertext, tag = encrypt(key, plaintext)
print(decrypt(key, ciphertext, tag)) 
