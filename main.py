import socket
import hashlib
import hmac
message2 = ("Secret Message!!!")

def generate_mac(key, message):

    key = bytes(key, 'utf-8')
    message = bytes(message, 'utf-8')
    return hmac.new(key, message, hashlib.sha512).hexdigest()

# original_message = "Important message"
secret_key = "ccnp"
original_mac = generate_mac(secret_key, message2)

s = socket.socket()
print("Socket successfully created!!!")
port = 56789
s.bind(("",port))
print(f"socket bind to port{port}")
s.listen(5)
print("Socket is listening")
while True:
    c, addr = s.accept()
    print("Got connection from",addr)
    c.send(message2.encode())
    c.send(original_mac.encode())
