import socket
import sys
from sys import argv
import time

if len(argv)!= 3:
    print 'Unknown parameters'
    print 'Usage python ./tcp_client.py <server_ip> <port>'
    sys.exit()

ip = argv[1]
port = int(argv[2])

print 'TCP client settings:\nServer IP:   %s\nPort: %d' % (ip, port)
print 'Please make sure above values are pointing to your board.\n'

# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(300)

try:
    # Connect the socket to the port where the server is listening.
    server_address = (ip, port)
    print 'Connecting to %s port %s...' % server_address
    sock.connect(server_address)

    # Send TCP packet to WINC1500 TCP server.
    print 'Sending TCP packet...'
    sock.sendall('Hello')
	
    # WINC1500 TCP server will echo received data back to client.
    data = sock.recv(1460)
    print 'Received', data, 'from WINC1500'
except (socket.error, socket.timeout) as msg:
    print 'Error - ',msg
finally:
    print 'closing socket'
    sock.close()
    sock = None
    sys.exit(1)
