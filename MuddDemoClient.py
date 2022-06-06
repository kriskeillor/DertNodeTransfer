# Kris Keillor
# Demonstration Script - Client
# Multi User Data Daemon (MUDD) library
# v0.2.0
# Prof. Junaid Khan
# EECE 397A Wireless Networking


#   *   *   *   *   *   *
# INCLUDES
#   *   *   *   *   *   *
from socket import *


#   *   *   *   *   *   *
# VARIABLES
#   *   *   *   *   *   *
# Network settings
localhost = "192.168.137.53"
tcpPort = 6545;
# Create TCP client
clientSocket = socket(AF_INET, SOCK_STREAM);
clientSocket.connect((localhost, tcpPort));


#   *   *   *   *   *   *
# PROGRAM
#   *   *   *   *   *   *
# Debug 
print("Socket: {}".format(clientSocket));
print("localhost: {}; port: {}".format(localhost, tcpPort));
# Send and receive a message
while True:
    msg = input("Please, write a message! ");
    clientSocket.send(msg.encode());
    msgMod = clientSocket.recv(1024);
    print("Response from server: " + msgMod.decode() + "\n");
connSocket.close();