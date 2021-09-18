def TopPorts():
 import os
 hostname = input("Enter the Ip add:-")
 response = os.system("nmap --top-ports 20 " + hostname)
 input("Press any key....")
TopPorts()