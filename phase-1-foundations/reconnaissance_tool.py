import socket
import csv

def scan_ports(target, start, end):
    open_port = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        for port in range(start, end):
            connected = sock.connect_ex((target, port))
            if connected == 0:
                open_port.append(port)
    return open_port

def identify_service(ports):
    protocol = ['tcp', 'udp']
    services = []
    for port in ports:
        try:
            service = socket.getservbyport(port, protocol[0])
            services.append(service)
        except OSError:
            service = socket.getservbyport(port, protocol[1])
            services.append(service)
    return services

def vulner_searcher(services):
    vulner = []
    with open('vulnerabilities.csv', 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            for service in services:
                if service.lower() == row[0].lower():
                    vulner.append(f"{service}: {row[2]} ({row[3]})")
    return vulner

def main():
    ip = input("Enter ip you want to scan: ")
    s_port = int(input("Enter the port you want to being the scan from: "))
    e_port = int(input("Enter the port you want to end the scan at: "))
    
    open_ports = scan_ports(ip, s_port, e_port)
    print(f"Open ports found: {open_ports}")
    
    services = identify_service(open_ports)
    print(f"Services identified: {services}")
    
    vulner = vulner_searcher(services)
    print(f"Vulnerabilities found: {vulner}")
    
    with open('vulnerability.txt', 'w') as file:
        for vulner in vulner:
            file.write(vulner)
    
    print("Done")

if __name__ == "__main__":
    main()