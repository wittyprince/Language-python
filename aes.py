import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

AES_SECRET_KEY = 'e75e2d3126357d031ddaf412f9110f66'  # 此处16|24|32个字符
IV = "1234567812345678"

# padding算法
# BS = len(AES_SECRET_KEY)
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s: s[0:-ord(s[-1:])]


class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    # 加密函数
    def encrypt(self, text):
        text = pad(text.encode(), AES.block_size)
        cipher = AES.new(self.key.encode(), self.mode, IV.encode())
        encrypted_text = cipher.encrypt(text)
        # cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        # self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        encoded = base64.b64encode(encrypted_text)
        return str(encoded, 'utf-8')

    # 解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cipher = AES.new(self.key.encode(), self.mode, IV.encode())
        plain_text = cipher.decrypt(decode)
        # cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        # plain_text = cryptor.decrypt(decode)
        decoded = unpad(plain_text, AES.block_size)
        return str(decoded, 'utf-8')


if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT()
    my_email = "admin"
    e = aes_encrypt.encrypt(my_email)
    print(my_email)
    print(e)
    d = aes_encrypt.decrypt(e)
    print(d)