def Get_Mac():
    import os
    hostname = input("Enter the Ip Address to Get Mac :-")
    response = os.system("ARP -a " + hostname)
    input("Press any key....")
Get_Mac()