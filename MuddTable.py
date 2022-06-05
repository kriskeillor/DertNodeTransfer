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
# DATA FUNCTIONS
#   *   *   *   *   *   *
# Bulk add-value to all rows
def append_values_bulk(fname_in, col_add, fname_out):
    data_out = []
    filestream_in = open_reader_stream(fname_in)
    with filestream_in:
        reader = csv.reader(filestream_in)
        headers = next(reader)
        data_out = [headers] + [row + [col_add] for i, row in enumerate(reader)]
    filestream_out = open_writer_stream(fname_out)
    with filestream_out:
        csv.writer(filestream_out, delimiter=",").writerows(data_out)

    return ERR_NONE


#   *   *   *   *   *   *
# FILE SYSTEM FUNCTIONS
#   *   *   *   *   *   *
# Read object
def open_reader_stream(fname):
    try:
        reader_str = open(fname, "rt", newline='')   # Open in "read text" mode, universal newline
        return reader_str
    except:
        print("Could not read file " + fname)
        sys.exit(ERR_NO_DATA)
# Write object
def open_writer_stream(fname):
    try:
        writer_str = open(fname, "wt", newline='')   # Open in "write text" mode, universal newline
        return writer_str
    except:
        print(fname)
        print("Could not write file {}".format(fname))
        sys.exit(ERR_NO_DATA)
