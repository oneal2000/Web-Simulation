import socket
import sys
MaxBytes=1024*1024
host ='127.0.0.1'
port = 11223
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(30)
client.connect((host,port))
inputData = sys.argv[1]
sendBytes = client.send(inputData.encode())
client.close()
