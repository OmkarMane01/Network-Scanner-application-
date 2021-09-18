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
    input("Press any key")

iptrack()