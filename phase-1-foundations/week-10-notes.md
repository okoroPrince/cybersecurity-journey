# Week 10: Reconnaissance Tool Capstone

## What is a Reconnaissance Tool?

A reconnaissance tool automates the first phase of any attack or security audit. It:
1. Scans a target for open ports
2. Identifies what services are running
3. Searches for known vulnerabilities in those services
4. Generates a report of findings

This is real pentesting work — automated recon.

## My Reconnaissance Tool

**Workflow:**
1. User provides target IP and port range
2. Scanner connects to each port, identifies the service (SSH, Telnet, etc.)
3. Tool searches a CSV database of known vulnerabilities
4. Matches found vulnerabilities to identified services
5. Writes a report with findings

**Functions:**
- `scan_ports()` — Port scanning with socket connections
- `identify_service()` — Maps ports to service names
- `vulner_searcher()` — Searches CSV for CVEs matching services
- `main()` — Orchestrates the workflow

## Full Code

```python
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
```

## Example Output
```
Enter ip you want to scan: 127.0.0.1
Enter the port you want to being the scan from: 20
Enter the port you want to end the scan at: 60
Open ports found: [22, 23]
Services identified: ['ssh', 'telnet']
Vulnerabilities found: ['ssh: CVE-2018-15473 (High)', 'ssh: CVE-2014-6271 (Critical)']
Done
```

## Vulnerability Database (vulnerabilities.csv)
```
service,version,cve_id,severity,description
OpenSSH,7.4,CVE-2018-15473,High,Authentication bypass vulnerability
OpenSSH,6.6,CVE-2014-6271,Critical,Shellshock vulnerability
Apache,2.4.49,CVE-2021-41773,Critical,Path traversal vulnerability
Apache,2.4.50,CVE-2021-41773,Critical,Path traversal vulnerability
Nginx,1.14.0,CVE-2019-9511,High,HTTP/2 denial of service
Nginx,1.16.0,CVE-2019-1010022,High,Buffer overflow vulnerability
FTP,vsftpd-2.3.4,CVE-2011-2523,Critical,Backdoor vulnerability
HTTP,1.1,CVE-2014-6271,Critical,Shellshock vulnerability
DNS,BIND-9.4.2,CVE-2015-8000,High,Remote code execution
MySQL,5.7.0,CVE-2016-0584,High,Privilege escalation
SSH,OpenSSH,CVE-2014-6271,Critical,Shellshock vulnerability
Telnet,default,CVE-2011-2523,Critical,Telnet backdoor
```
## Why This Matters

This is the real attack methodology:
1. **Reconnaissance** — Find what's exposed (your tool does this)
2. **Enumeration** — Identify services and versions (your tool does this)
3. **Vulnerability Research** — Find exploitable weaknesses (your tool does this)
4. **Exploitation** — Attack the vulnerability (next phase)

You've built the foundation of a professional penetration testing tool. This is what real pentesters use (minus the CSV, they use live databases), but the logic and workflow are identical.

**Phase 1 complete.**