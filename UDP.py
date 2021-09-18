def Udp():
 import os
 hostname = input("Enter the Ip add:-")
 response = os.system("nmap -sU -p  " + hostname)
 input("Press any key....")
Udp()