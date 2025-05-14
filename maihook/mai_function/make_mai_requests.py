import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from ..constant.config_loader import mai_config
import hashlib
def obfuscate(src_str):
    return hashlib.md5((src_str + mai_config.mai2Salt).encode('utf-8')).hexdigest()

def aes_encrypt(data):
    key = mai_config.aesKey.encode('utf-8')
    iv = mai_config.aesIV.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))

def aes_decrypt(data):
    key = mai_config.aesKey.encode('utf-8')
    iv = mai_config.aesIV.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data), AES.block_size).decode('utf-8')

async def make_mai_request(api, data, user_id):
    entry = obfuscate(api)
    body = zlib.compress(aes_encrypt(data))
    cl = str(len(body))
    headers = {
        'Accept':'',
        'Accept-Encoding':'',
        'Host': mai_config.mai2Host,
        'User-Agent': f'{entry}',
        'charset': 'UTF-8',
        'Mai-Encoding': '1.40',
        'Content-Encoding': 'deflate',
        "Expect":"100-continue",
        'Content-Length': cl,
    }
