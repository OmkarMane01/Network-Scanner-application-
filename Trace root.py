def TraceRoot():
 import os
 hostname = input("Enter ip address to Trace Route:-")
 response = os.system("tracert " + hostname)
 print(response)
 input("Press any key.....")
TraceRoot()
