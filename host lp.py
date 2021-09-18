def HostList():
 import os
 hostname = input("Enter an ip:-")
 response = os.system("nmap -sL " + hostname +"/24")
 input("press any key...")
HostList()