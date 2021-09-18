def DetectOS():
 import os
 hostname = input("Enter the Ip add:-")
 response = os.system("nmap -A " + hostname)
 input("Press any key....")
DetectOS()