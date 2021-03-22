"""
Find Domain Name From DNS Pointer (PTR) Records Using IP Address
Write a function that takes an IP address and returns the domain name using PTR DNS records.

Example
get_domain("8.8.8.8") ➞ "dns.google"

get_domain("8.8.4.4") ➞ "dns.google"


Notes
You may want to import socket.
Don't cheat and just print the domain name, you need to make a real DNS request.
Return as a string.
"""



################################################################
"""
Solution 1
"""


import socket as sk
def get_domain(ip_address):
	return sk.getfqdn(sk.gethostbyaddr(ip_address)[0])



################################################################
"""
Solution 2
"""


def get_domain(ip_address):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip_address, 80))
    s.close()
    domain = socket.gethostbyaddr(ip_address)[0]
    return domain



################################################################
"""
Solution 3
"""


import socket
def get_domain(ip_address):
	return socket.getnameinfo((ip_address, 0), 0)[0]






