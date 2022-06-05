# Kris Keillor
# Table (CSV) Script
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
    import datetime
except ImportError:
    print("Datetime module import failed")
    sys.exit(ERR_GENERIC)
try:
    import csv
except ImportError:
    print("CSV module import failed")
    sys.exit(ERR_GENERIC)
#   *   *   *   *   *   *


#   *   *   *   *   *   *
# VARIABLES
#   *   *   *   *   *   *
# File objects
try:
    fin_name = "DataStreams/SampleDertData.csv"
    filestream_in = open(fin_name, "rt", newline='')
except:
    print("No sample data to modify")
    sys.exit(ERR_NO_DATA)
try:
    fout_name = "DataStreamsFiltered/SampleDertDataFiltered.csv"
    filestream_out = open(fout_name, "wt", newline='')
except:
    print("Unable to open output file")
    sys.exit(ERR_TIMEOUT)


#   *   *   *   *   *   *
# FUNCTIONS
#   *   *   *   *   *   *
# Bulk add-value to all rows
def append_values_bulk(to_add):
    data_out = []
    with filestream_in:
        reader = csv.reader(filestream_in)
        headers = next(reader)
        data_out = [headers] + [row + [to_add] for i, row in enumerate(reader)]
    with filestream_out:
        csv.writer(filestream_out, delimiter=",").writerows(data_out)

    return ERR_NONE


#   *   *   *   *   *   *
# PROGRAM
#   *   *   *   *   *   *
append_values_bulk("")   # Add a blank (3rd) entry to each row