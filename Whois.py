def Wia():
    import whois
    data = input("Enter a domain: ")
    w = whois.whois(data)
    print(w)
    input("Press any key.....")
Wia()
