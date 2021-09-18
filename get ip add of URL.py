def Url():
 import socket
 ip = input("Enter your Domain:-")
 print(socket.gethostbyname(ip))
 print("Press any key to clear!!")
Url()
