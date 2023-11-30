# import socket
#
# #we need to specify the private ip address with variables
# HOST = "192.168.184.1"
# PORT = 9090
# #BUILDING A TCP SOCKET
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
#
# server.listen(1)
#
# while True:
#     communication_socket, address = server.accept()
#     #after we get a connection
#     print(f"Connected to {address}")
#     message = communication_socket.recv(1024).decode('utf-8')
#     print(f"Message from client is: {message}")
#     communication_socket.send(f"Got your message! Thank you".encode('utf-8'))
#     #we need to introduce multithreading TCP CHAT OR CAMERA STREAMING, TCP CHAT
#     communication_socket.close()



import socket
#will be used to create an effiecient link with the server socket to plug us in

#if the client is in the local area network, you just connect to the server ip address
#Otherwise we need the ip address the public ip adress if the device is outside the LAN

# ip address
HOST = "192.168.106.1"
PORT = 9098
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)

while True:
    #we accept the message
    socket_mess,address = server.accept()
    print(f"You are connected to the following address{address}")
    message = input("Enter the message to tell the client what to do!")
    #we want to send the message to the client
    socket_mess.send(message.encode('utf-8'))
    #we want to receive what the client is going to say
    clientMess = socket_mess.recv(1024)
    print(f"The Client message is:{clientMess.decode('utf-8')}")
    socket_mess.close()
#close the server
# server.close()















