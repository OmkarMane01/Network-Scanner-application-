import os
import urllib3
import json

http = urllib3.PoolManager()
while True:
    ip = input("Enter the IP Adress:-")
    url = http.request('POST', 'http://ip-api.com/json/', fields={'ip'})

    values = json.loads(url.data)

    print("IP" + values['query'])
    print("City" + values['city'])
    print("ISP" + values['isp'])

    break
