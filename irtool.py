import sys
import os
import time



print("""\033[1;32;40m

				  ___ ____ _____           _ 
				 |_ _|  _ \_   _|__   ___ | |
				  | || |_) || |/ _ \ / _ \| |
				  | ||  _ < | | (_) | (_) | |
				 |___|_| \_\|_|\___/ \___/|_|
			                             
		                                            

		******************************************************************
		# First/Basic linux incident handling tool for Sysadmin or users #
		# Github https://github.com/GULIY3V
		******************************************************************

\n""")

print("\033[0;0m")

time.sleep(3)
system = sys.version_info.major
if system == 3:
	print ("Please run the script for Python 2 version")
print("""\033[1;32;40m

	     	     [+] Logined users\n
						""")

print("\033[0;0m")
who = os.system("who")
print("""\033[1;32;40m

	     	     [+] ARP machine names and MAC adresses\n
						""")

print("\033[0;0m")
arp = os.system("arp -an")
print("""\033[1;32;40m

	     	     [+] Saved suspicious DNS\n
						""")

print("\033[0;0m")
dns = os.system("cat /etc/resolv.conf")
print("""\033[1;32;40m

	     	     [+] List suspicious connections\n
						""")

print("\033[0;0m")
conn = os.system("lsof -i")
print("""\033[1;32;40m

	     	     [+] Last logined\n
						""")

print("\033[0;0m")
login = os.system("lastlog")
print("""\033[1;32;40m

	     	     [+] Cron jobs\n
						""")

print("\033[0;0m")
cron = os.system("ls /etc/cron.*")
print("""\033[1;32;40m

	     	     [+] Last commands for user\n
						""")

print("\033[0;0m")
lastcom = os.system("lastcomm | more")
print("""\033[1;32;40m

	     	     [+] Login/Logout log\n
						""")

print("\033[0;0m")
loginlogout = os.system("last -f /var/log/wtmp")

