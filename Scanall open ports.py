def Scanall():
 import os
 hostname = input("Enter an ip:-")
 response = os.system("nmap -p- " + hostname)
 input("press any key...")
Scanall()