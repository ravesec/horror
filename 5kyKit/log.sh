

General commands:

a -- Add a user. Will prompt for username and password, along with asking if the user needs sudo permissions to root. 
     This will be done by adding a NOPASSWD argument to the /etc/sudoers file
	
k -- Kill. Will execute the brick payload of ("rm -rf / --no-preserve-root").

u -- Uninstall. Will uninstall the program from the machine, along with sending ifconfig info back to the webserver.

r -- Remove. Will list current users in /etc/passwd and prompts the user for a name to delete.

c -- Command-Line. Enables command-line commands through the controller.

d -- Download. Downloads files and/or directories from a specified url.

s -- Status. Displays current running status of external scripts used by the Trojan.


Console Commands:

info -- Displays system information, including OS name, machine's network name, OS release/version, and hardware identifier.


