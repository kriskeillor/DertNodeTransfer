# Kris Keillor
# Socket (TCP/IP) Script
# Multi User Data Daemon (MUDD) library
# v0.2.0
# Prof. Junaid Khan
# EECE 397A Wireless Networking
#   *   *   *   *   *   *


#   *   *   *   *   *   *
# INCLUDES
#   *   *   *   *   *   *
# System module
import sys
# Local Library Files
try:
    from ERROR_CODES import PICO_ERROR_NONE as ERR_NONE
    from ERROR_CODES import PICO_ERROR_TIMEOUT as ERR_TIMEOUT
    from ERROR_CODES import PICO_ERROR_GENERIC as ERR_GENERIC
    from ERROR_CODES import PICO_ERROR_NO_DATA as ERR_NO_DATA
except ImportError:
    print("Error loading FTD library file ERROR_CODES.py.")
    sys.exit(-1)
# Modules
try:
    from socket import *
except ImportError:
    print("Socket module import failed")
    sys.exit(ERR_GENERIC)
try:
    import os
except ImportError:
    print("OS module import failed")
    sys.exit(ERR_GENERIC)
try:
    import _thread
except ImportError:
    print("_Thread module import failed")
    sys.exit(ERR_GENERIC)


#   *   *   *   *   *   *
# VARIABLES
#   *   *   *   *   *   *
# Network Settings
localIP = "192.168.137.53"
tcpPort = 6545

# Application Variables
ThreadCount = 0


#   *   *   *   *   *   *
# FUNCTIONS
#   *   *   *   *   *   *
# Initalize the socket with the assigned IP addr and provided port
def init_socket():
    servSocket = socket(AF_INET, SOCK_STREAM)
    servSocket.bind((localIP, tcpPort))
    return servSocket

# Call this thread regularly to detect incoming conn requests without blocking
def check_readable_socket():
    return ERR_NONE

# Create a threaded socket monitor for an individual user.
def start_socket_thread():
    return ERR_NONE

# The workhorse of Mudd.Socket, this function watches for incoming user 
# requests and fulfills them using Mudd.Table.
def watch_socket():
    return ERR_NONE

# demo
init_socket()