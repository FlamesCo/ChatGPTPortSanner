import socket

def scan_ports(host, start, end):
    open_ports = []
    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    if len(open_ports) == 0:
        print("404: No open ports found.")
        return None
    else:
        return open_ports

if __name__ == "__main__":
    try:
        host = input("Enter the host to scan: ")
        start = int(input("Enter the starting port: "))
        end = int(input("Enter the ending port: "))
        open_ports = scan_ports(host, start, end)
        if open_ports is None:
            pass
        else:
            print("Open ports:", open_ports)
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
