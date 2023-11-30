# import socket
#
#
# HOST = '192.168.184.1'
# PORT = 9090
#
# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.connect((HOST, PORT))
#
# socket.send("Hello World!".encode('utf-8'))
# print(socket.recv(1024).decode('utf-8'))




#this is the client, I receive a meesage from the server and tell it something in return
#Let's Get it
import socket
PORT = 9098
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.106.1", PORT))

messageFomServer = client.recv(1024)
print(f"Message:{messageFomServer.decode('utf-8')}")
talkToServer = input("Enter the response to the Server")
print(talkToServer.encode('utf-8'))














