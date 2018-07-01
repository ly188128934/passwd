import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',6161))
print (s.recv(1024).decode('utf-8'))
data = ['11','22','33']
# for data in [b'bob',b'mike',b'john']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
s.send(data)
s.send(b'exit')
s.close