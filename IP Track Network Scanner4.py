def IPTrackNetworkScanner():
 import socket
 import sys
 import os
 os.system("title Network Scanner V1.0.01")
 os.system("color 02")
 print("#"*72)
 print("""                       *Version :1.0.01*
 _______________________________________________________________________
 |  _   _    ____        __  ____                                  _    |
 | | \ | |  / /\ \      / / / ___|  ___ __ _ _ __  _ __   ___ _ __| |   |
 | |  \| | / /  \ \ /\ / /  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| |   |
 | | |\  |/ /    \ V  V /    ___) | (_| (_| | | | | | | |  __/ |  |_|   |
 | |_| \_/_/      \_/\_/    |____/ \___\__,_|_| |_|_| |_|\___|_|  (_)   |
 |______________________________________________________________________|""")
 print()
 h = socket.gethostname()
 puip = socket.gethostbyname(socket.getfqdn())
 print("[+]Your Host Machine Name:-",h,"  |[+]Developed by D.O.T(MS.c-I Year)")
 print("[+]Your Public IP:-",puip,"|[+]Rachan,Omkar,Mayuri")
 print("#"*72)
 print("\t\tWelcome To In IP Track Network Scanner. ")
 print("." * 72)
 print("\n\t\t\t\t*MENU* ")
 print("[1].Host-list Network with IP           [2].Exit")
 print("." * 72)


IPTrackNetworkScanner()