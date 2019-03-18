
from socket import *

# build tcp connection
serverName = '169.254.61.87'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# request file from server
print("Request file test.txt.....")
file_name = "test.txt"
clientSocket.send(file_name.encode())

# print file content or error information
rcv_file = clientSocket.recv(1024)
print("From Server:", rcv_file.decode())

# close socket connection
clientSocket.close()

