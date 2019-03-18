
from socket import *
import os

# create socket to listen
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('169.254.61.87',serverPort))
serverSocket.listen(1)

print ("The server is ready to receive")

while True:
    # get connected socket
    connectionSocket, addr = serverSocket.accept()

    # get request file name
    file_name = connectionSocket.recv(1024).decode()
    # build full file path
    file_path = os.path.join(os.getcwd(), file_name)

    content = ""

    # open and read the file
    try:
        f = open(file_path, 'r')
        try:
            content = f.read()
        finally:
            f.close()
    except IOError as e:
        print(e)
        content = "Error: 没有找到文件或读取文件失败"
        
    # send content
    connectionSocket.send(content.encode())

    connectionSocket.close()

