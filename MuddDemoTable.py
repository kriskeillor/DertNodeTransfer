# Kris Keillor
# Demonstration Script - Table Functions
# Multi User Data Daemon (MUDD) library
# v0.4.0
# Prof. Junaid Khan
# EECE 397A Wireless Networking


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
    print("Error loading MUDD library file 'ERROR_CODES.py.'")
    sys.exit(-1)
try:
    from MuddTable import append_values_bulk, append_entry, print_stream
except ImportError:
    print("Error loading MUDD library file MuddTable.py")
    sys.exit(ERR_GENERIC)
try:
    import MuddSocket
except ImportError:
    print("Error loading MUDD library file MuddSocket.py")
    sys.exit(ERR_GENERIC)
# Modules
import os
try:
    import random
except ImportError:
    print("Random module import failed")
    sys.exit(ERR_GENERIC)
try:
    import time
except ImportError:
    print("Time module import failed")
    sys.exit(ERR_GENERIC)
try:
    import _thread
except ImportError:
    print("_Thread module import failed")
    sys.exit(ERR_GENERIC)
try:
    from pathlib import Path
except ImportError:
    print("Pathlib.Path module import failed")
    sys.exit(ERR_GENERIC)


#   *   *   *   *   *   *
# VARIABLES
#   *   *   *   *   *   *
# File objects
fin_dir = "DataStreams/"
fout_dir = "DataStreamsFiltered/"
fname_test1 = "SampleDertData01"
fname_test2 = "SampleDertData02"
fname_test3 = "SampleDertData03"
dat_ext = ".csv"
# Socket settings
maxUsers = 3
localIP = "192.168.137.53"
tcpPort = 6545
ThreadCount = 0


#   *   *   *   *   *   *
# PROGRAM
#   *   *   *   *   *   *
# File 1 copy - adding comma
f1r = fin_dir+fname_test1+dat_ext
f1w = fout_dir+fname_test1+"Out"+dat_ext
append_values_bulk(f1r, "", f1w)    # Add a blank value to each row

# File 2 append - add datetime entry
f2a = fin_dir+fname_test2+dat_ext
append_entry(f2a, "LUX", 5000)      # Add a row to the table

# File 3 append loop
f3a = fin_dir+fname_test3+dat_ext
f3a_made = True                     # Already created demo output
if not f3a_made:
    for i in range(1, 60):
        atf = random.randrange(5000, 9500)/100
        arh = random.randrange(0, 100)/100
        lux = random.randrange(4650, 50000)
        stc = random.randrange(6000, 9000)/100
        swc = random.randrange(0, 100)/100
        append_entry(f3a, "ATF", atf)
        append_entry(f3a, "ARH", arh)
        append_entry(f3a, "LUX", lux)
        append_entry(f3a, "STC", stc)
        append_entry(f3a, "SWC", swc)
        time.sleep(10)  # Wait for the sensor period
        print_stream(f3a)# demo