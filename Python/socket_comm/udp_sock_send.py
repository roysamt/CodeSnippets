import socket

DEST_IP = "127.0.0.1"
DEST_PO = 5000

messages = ["msg1", "msg2", "msg3"]

#Transmit
print "Target: ", DEST_IP, " : ", DEST_PO

sock = socket.socket(socket.AF_INET, # IPv4
					 socket.SOCK_DGRAM) # UDP
sock.connect((DEST_IP, DEST_PO))

for i in messages:
        print "Sending ", i
        sock.sendall(i)
        time.sleep(0.5)
