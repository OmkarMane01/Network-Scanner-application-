def Tcp():
 import os
 hostname = input("Enter the Ip add:-")
 response = os.system("nmap -sT " + hostname)
 input("Press any key....")
Tcp()