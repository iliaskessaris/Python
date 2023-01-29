import socket
import threading

# choose nickname
nickname = input("Επέλεξε το ψευδώνυμό σου: ")
SERVER = socket.gethostbyname(socket.gethostname())
# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((socket.gethostname(), 55555))
client.connect((SERVER, 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Προέκυψε ένα λάθος!')
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
