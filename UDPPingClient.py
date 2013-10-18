
__author__ = 'Phuoc Huynh, Romer Ibo'

from socket import *
from time import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

for i in range(1,11):
    message = "Ping " + str(i) + " " + str(ctime())
    print message
    try:
        clientSocket.settimeout(1.0)
        start_time = clock()
        clientSocket.sendto(message,(serverName,serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        rtt = clock() - start_time
        print "RTT", rtt
        print "Server responded:", modifiedMessage
    except timeout:
        print "Request timed out"
clientSocket.close();
