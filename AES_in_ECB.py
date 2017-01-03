import base64
import os
from Crypto.Cipher import AES

key = b"YELLOW SUBMARINE"
crypt = base64.b64decode(open(os.path.dirname(__file__) + '../ch7.txt', 'r').read())
cipher = AES.new(key, AES.MODE_ECB)
out = cipher.decrypt(crypt)
print(out)