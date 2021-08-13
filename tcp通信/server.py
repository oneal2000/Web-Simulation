import socket
MaxBytes = 1024 * 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 120分钟的timeout
server.settimeout(60*120)
host = '127.0.0.1'
port = 11223
server.bind((host, port))
server.listen(1)
while True:
    client,addr = server.accept()
    while True:
        data = client.recv(MaxBytes)
        if not data:
            break
        rev_msg=(data.decode())
        print(rev_msg)


