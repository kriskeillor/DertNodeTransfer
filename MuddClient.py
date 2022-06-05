# Kris Keillor
# Client Script
# Multi User Data Daemon (MUDD) library
# v0.2.0
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
    from MuddTable import append_values_bulk
except ImportError:
    print("Error loading MUDD library file MuddTable.py")
    sys.exit(-1)


#   *   *   *   *   *   *
# VARIABLES
#   *   *   *   *   *   *
# File objects


#   *   *   *   *   *   *
# PROGRAM
#   *   *   *   *   *   *
# File 1 read/write
