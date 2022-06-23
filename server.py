import socket

s = socket.socket()
print("socket successfully created")

port = 12345
s.bind(('',port))
print("socket binded to", port)

s.listen(5)
print("socket is listening")

while True:
  c, addr = s.accept()
  print('Got connection from', addr)
  c.send('Thank you for connecting'.encode())
  c.close()
  break
