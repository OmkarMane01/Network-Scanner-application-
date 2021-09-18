import os
def NetworkScanner():
 import socket
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
 print("\t\tWelcome To In  Network Scanner. ")
 print("." * 72)
 print("\n\t\t\t\t*MENU* ")
 print("[1].LAN Network Scanner             [2].WEB Network Scanner")
 print("[3].Other Network Scanner           [4].IP Track Network Scanner")
 print("                         [5].Exit")
 print("." * 72)
NetworkScanner()
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
 print("[1].IP Track Location                [2].Exit")
 print("." * 72)
def iptrack():
    import os
    import urllib3
    import json
    http = urllib3.PoolManager()
    while True:
        ip = input("Enter the IP Adress:-")
        url = http.request('POST', 'http://ip-api.com/json/', fields={'ip'})

        values = json.loads(url.data)

        print("IP:-" + values['query'])
        print("Status:-" + values['status'])
        print("Country:-" + values['country'])
        print("Country-Code:-" + values['countryCode'])
        print("Region:-" + values['region'])
        print("RegionName:-" + values['regionName'])
        print("City:-" + values['city'])
        print("Zip-Code:-" + values['zip'])
        print("Latitude:-")
        print(float(values['lat']))
        print("Longitude:-")
        print(float(values['lon']))
        print("Time-Zone:-" + values['timezone'])
        print("Internet-Service-Provider:-" + values['isp'])
        print("Organization-Name:-" + values['org'])
        print("AS-Organization,:-" + values['as'])
        break




loop = 1
while loop == 1:
    ch = int(input("Please select the option :"))
    if ch == 1:
        print("LAN Network Scanner  ")
        input("press any key to Clear........")
        os.system('cls')
        NetworkScanner()
    elif ch == 2:
        print("WEB Network Scanner  ")
        input("press any key to Clear........")
        os.system('cls')
        NetworkScanner()
    elif ch == 3:
        print("Other Network Scanner  ")
        input("press any key to Clear........")
        os.system('cls')
        NetworkScanner()
    elif ch == 4:
        os.system('cls')
        IPTrackNetworkScanner()
        loop4 = 1
        while loop4 == 1:
            ch4 = int(input("Please select the option :"))
            if ch4 == 1:
                iptrack()
                input("press any key to Clear........")
                os.system('cls')
                IPTrackNetworkScanner()
            elif ch4 == 2:
                loop4 = 0
                print("Thank So Much !")
                input("press any key to Exit........")
                os.system('cls')
                NetworkScanner()
            else:
                print("Enter R8 no betwwen 1 to 5!")
                input("press any key to Clear........")
                os.system('cls')
                IPTrackNetworkScanner()
                os.system('cls')
                NetworkScanner()
    elif ch == 5:
        loop = 0
        print("Thank So Much !")
        input("press any key to Exit........")
        os.system('cls')
    else:
        print("Enter R8 no betwwen 1 to 5!")
        input("press any key to Clear........")
        os.system('cls')
        NetworkScanner()
