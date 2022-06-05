# Kris Keillor
# DSC Datetime Generator
# v0.1.0
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
    from ERROR_CODES import DERT_ERROR_NONE, DERT_ERROR_TIMEOUT, DERT_ERROR_GENERIC, DERT_ERROR_NO_DATA
except ImportError:
    print("FTD library file ERROR_CODES.py not located.")
    sys.exit(-1)
# Modules
try:
    import datetime
except ImportError:
    print("Datetime module import failed")
    sys.exit(DERT_ERROR_GENERIC)
try:
    import csv
except ImportError:
    print("CSV module import failed")
    sys.exit(DERT_ERROR_GENERIC)
#   *   *   *   *   *   *


#   *   *   *   *   *   *
# VARIABLES
#   *   *   *   *   *   *
# File objects
try:
    fin_name = "DataStreams/SampleDertData.csv"
    filestream_in = open(fin_name, "rt")
except:
    print("No sample data to modify")
    sys.exit(DERT_ERROR_NO_DATA)
try:
    fout_name = "DataStreamsFiltered/SampleDertData.csv"
    filestream_out = open(fout_name, "wt")
except:
    print("Unable to open output file")
    sys.exit(DERT_ERROR_TIMEOUT)
# CSV objects
with filestream_in:
    reader = csv.reader(filestream_in)
with filestream_out:
    reader = csv.reader(filestream_out)