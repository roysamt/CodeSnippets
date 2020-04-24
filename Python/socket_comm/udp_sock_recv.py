import socket, select
  
SRC_PORT = 5000

sock = socket.socket(socket.AF_INET, # IPv4
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', SRC_PORT))
sock.setblocking(0)

while True:
    print "Listening..."
    result = select.select([sock],[],[])
    msg = result[0][0].recv(64) 
    print (msg)
