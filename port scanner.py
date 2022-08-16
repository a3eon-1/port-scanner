from ipaddress import ip_address
import socket

ip_address = input("Enter IP address: ")
lower_port = int(input("Enter lower port: "))
upper_port = int(input("Enter upper port: "))


for port in range(lower_port, upper_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip_address, port))
    if result == 0:
        print("Port " + str(port) + " is open")
    else:
        print("Port " + str(port) + " is closed")