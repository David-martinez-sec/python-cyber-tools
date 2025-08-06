# basic_port_scanner.py

import socket
from datetime import datetime

# Get the target IP or hostname
target = input("Enter target IP or hostname: ")

# Resolve the IP (in case a hostname was used)
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

print(f"Scanning target: {target_ip}")
print("Scanning ports 1-1024...\n")

# Timestamp start
start_time = datetime.now()

# Scan ports 1–1024
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"[+] Port {port} is open ({service})")
    s.close()


# Timestamp end
end_time = datetime.now()
print(f"\nScanning completed in: {end_time - start_time}")
