import socket

# connection opening using the socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.google.com',80))
print("Enter the url from where you would like to fetch the data")
url = str(input())
url = 'GET '+url+' HTTP/1.0\n\n'
cmd = url.encode()
mysock.send(cmd)

while(True):
    # n characters at a time , here n = 512
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())

# close the connection that was closed by closing the socket
mysock.close()