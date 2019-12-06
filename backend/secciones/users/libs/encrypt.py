import binascii
from Crypto.Cipher import AES
from Crypto import Random


class Encryption:
    @staticmethod
    def encrypt(message):
        msglist = []
        key = bytes("theterosnest2020", "utf-8")
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        msg = iv + cipher.encrypt(bytes(message, "utf-8"))
        msg = binascii.hexlify(msg)
        for letter in str(msg):
            msglist.append(letter)
        msglist.remove("b")
        msglist.remove("'")
        msglist.remove("'")
        return ''.join(msglist)
    @staticmethod
    def decrypt(message):
        msglist = []
        key = bytes("theterosnest2020", "utf-8")
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        msg = cipher.decrypt(binascii.unhexlify(bytes(message, "utf-8")))[len(iv):]
        for letter in str(msg):
            msglist.append(letter)
        msglist.remove("b")
        msglist.remove("'")
        msglist.remove("'")
        return ''.join(msglist)
