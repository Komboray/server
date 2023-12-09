import socket
import threading

nickname = input("Choose a nickname:")
if nickname == 'admin':
    password = input("Enter password for the admin")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5050))

#receive function that is running constantly

stop_thread = False
def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == "RAY":
                client.send(nickname.encode('ascii'))
                next_messo = client.recv(1024).decode('ascii')
                if next_messo == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print(f'Connection was refused, wrong password was used')
                        stop_thread = True
                elif next_messo == 'BAN':
                    print('Connection refused because of ban!')
                    client.close()
                    stop_thread = True
            else:
                print(message)

        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("")}'
        #check if the message starts with slash kick, we are going to skip the length of the nickname and then add two more characters
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
                #we send message to the server
                if message[len(nickname)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname)+2+6]}'.encode('ascii'))

                elif message[len(nickname)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(nickname)+2+5:]}'.encode('ascii'))
            else:
                print("Commands can only be executed by the admin")
        else:
            #if an orrdinary message we are going to send it to the server
            client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

