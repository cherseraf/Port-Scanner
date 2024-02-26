import socket

ip = input("Please enter the IP address you want to scan: ")
for port in range(1,65536):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = s.connect_ex((ip, port))
	if result == 0:
		print("{} is open!".format(port))
