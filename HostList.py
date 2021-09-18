def Hostlist():
 import nmap
 ip = input("Enter Your Default Gateway:-")
 if len(ip) == 0:
     print("!!!You Not Enter IP!!!")
 else:
     network = ip + "/24"
     print("Sacnning Reqwired Please Wait.......")

     nm = nmap.PortScanner()
     nm.scan(hosts=network, arguments='-sn')
     host_list =[(x,nm[x]['status']['state']) for x in nm.all_hosts()]
     for host, status in host_list:
         print("Host:\t{}".format(host))
 input("Press any key......")
Hostlist()