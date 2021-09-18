def design():
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
 print("[+]Your Host Machine Name:-",h,"\t\t\t\t developed by DOT")
 print("[+]Your Public IP:-",puip,"\t\t\t\t MS.c_I Year ")
 print("#"*72)

design()
input("press any key")
