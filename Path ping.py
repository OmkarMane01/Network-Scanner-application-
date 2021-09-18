def PathPing():
 import os
 hostname = input("Enter the Ip add:-")
 response = os.system("pathping " + hostname)
 input("Press any key....")

PathPing()
