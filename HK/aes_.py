from Crypto.Cipher import AES

#server encrypt
def do_encrypt(message):
    obj = AES.new("123",AES.MODE_CBC, "456")
    ciphertext = obj.encrypt(message)
    return ciphertext

# client de encrypt
def do_encrypt(ciphertext):
    obj = AES.new("123", AES.MODE_CBC, "456")
    messages = obj.decrypt(ciphertext)
    return messages