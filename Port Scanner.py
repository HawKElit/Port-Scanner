import socket
import threading

ip_addy = input("Please enter your IP address: ")
open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip_addy, port))
    if result == 0:
        open_ports.append(port)
        print(f"[*] Port {port} is OPEN")
    s.close()

print(f"Scanning {ip_addy}...")

threads = []
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nScan complete. {len(open_ports)} open ports found.")