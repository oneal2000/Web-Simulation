import socket
import time
MaxBytes=1024*1024
host ='127.0.0.1'
port = 11223
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(30)
client.connect((host,port))
while True:
    inputData=input()       #等待输入数据
    if(inputData=="quit"):
        print("我要退出了，再见")
        break
    sendBytes = client.send(inputData.encode())
    if sendBytes<=0:
        break
    recvData = client.recv(MaxBytes)
    if not recvData:
        print('接收数据为空，我要退出了')
        break
    localTime = time.asctime( time.localtime(time.time()))
    print(localTime, ' 接收到数据字节数:',len(recvData))
    print(recvData.decode())
client.close()
