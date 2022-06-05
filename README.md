# MUDD Library
The Multi User Data Daemon (MUDD) library is a straightforward collection of Python scripts meant to be called by IoT sensor applications. It can read raw sensor data and log messages, tabulate them, discard bad entries, and respond to requests for data. The responses are stored in shared folders accessible over [Samba](https://www.samba.org/samba/what_is_samba.html). 

The MUDD library utilizes the TCP/IP protocols in its `MuddSocket` script, but relies on the underlying Raspberry Pi computer running Samba over the SMB/CIFS protocol for sharing files. The `MuddTable` script processes CSV files. 
