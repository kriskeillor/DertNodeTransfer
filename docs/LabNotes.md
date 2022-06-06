# Project Report

## Using SSH 
    - Generated keys using PuttyGEN
    - Transferred to `C:\Users\Administrator\.ssh` as "id_rsa" and "id_rsa.pub"
    - Added public key to github
    - Rewrote upstream git url to be "git@github.com:user/repo.git"

## Using Python Files
Note that the script currently cannot gracefully create the output CSV directory if it is missing.

## Using Samba
Samba was installed using:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install samba samba-common-bin
```

The final output is logged as [apt-get-samba](apt-get-samba.log). The config file is located at `/etc/samba/smb.conf`. After the program was installed, a share drive was created with:

```
sudo mkdir -m 1777 /iotshare
```

and the contents of [iotshare](iotshare.conf) appended to the smb config file.

Finally, a Samba user/password is created and the Samba service restarted:

```
sudo smbpasswd -a pi
sudo /etc/init.d/smbd restart
```

Note that the last command is slightly different than reference [2] defines, as the service on my installation was named "smbd" instead of "samba".

To connect to the drive - the exciting part! - I had to map a network drive with the address \\IP\user\iotshare, checking "Use different credentials" and logging in with the user/password combination made earlier. A quick file touch demonstrated the successful file share, as shown in [SambaShareHelloWorld](SambaShareHelloWorld.png)!

References:
1. https://raspberrypihq.com/how-to-share-a-folder-with-a-windows-computer-from-a-raspberry-pi/

2. https://magpi.raspberrypi.com/articles/samba-file-server

## Using the `Select()` System Call

References:
1. https://stackoverflow.com/questions/5308080/python-socket-accept-nonblocking