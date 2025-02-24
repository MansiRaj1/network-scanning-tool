#!/usr/bin/python3
import socket
# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)  # Set timeout for socket operations
# Get user input for host
host = input("[*] Enter The Host To Scan: ")
# Function to scan a given port
def portscanner(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set timeout for each connection attempt
        if s.connect_ex((host, port)):  # If connection fails, port is closed
            print(f"[!!] Port {port} is closed")
        else:  # If connection succeeds, port is open
            print(f"[+] Port {port} is open")
# Loop through ports 1 to 99
for port in range(1, 100):
    portscanner(port)
