def OpenPort():
 import os
 hostname = input("Enter the Ip add:-")
 response = os.system("nmap -sV " + hostname)
 input("Press any key....")
OpenPort()