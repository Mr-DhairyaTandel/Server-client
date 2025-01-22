import socket
import hashlib
import hmac
s = socket.socket()
port = 56789
s.connect(("127.0.0.1",port))
recieve1 = s.recv(1024)
message2 = (recieve1.decode("utf-8"))
secret_key = str("ccnp")
recieve2 =(s.recv(1024))
external_mac= (recieve2.decode("utf-8"))
print("recieved message is: ",message2)
print("External mac is: ",external_mac)
def generate_mac(key, message):
    key = bytes(key, 'utf-8')
    message = bytes(message, 'utf-8')
    return hmac.new(key, message, hashlib.sha512).hexdigest()


original_mac1= generate_mac(secret_key, message2)
original_mac = str(original_mac1)
print ("Orignal mac is: ",generate_mac(secret_key, message2))
print(message2)
# external_mac = s.recv(1024)

# Verify
if external_mac == original_mac:
    print("Message is authentic.")
else:
    print("Message has been tampered with.")
