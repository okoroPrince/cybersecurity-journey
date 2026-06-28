# Week 4: Nmap & Network Reconnaissance

## What is Nmap?
Nmap is a network reconnaissance tool used in cybersecurity to scan networks and discover what devices/services are running and what ports are open.

## Key Commands
- **`nmap -sn 10.0.2.0/24`** — Ping scan. Checks which hosts are alive on a network without scanning ports.
- **`nmap -p- 127.0.0.1`** — Port scan. Scans all 65,535 ports on a target machine to find open ports.

## What I Found
When I scanned my VM (127.0.0.1), I found:
- **Port 631 (open)** — Internet Printing Protocol (IPP) service running
- **65,534 ports (closed)** — No services on these ports

## Understanding Ports
A port is like a door to a service on a computer. Each service (web server, printer, SSH, etc.) listens on a specific port.

- **Open port** = service is listening, potential attack surface
- **Closed port** = nothing listening, safer

## Open Port ≠ Vulnerability
Just because a port is open doesn't automatically mean it's exploitable. You need to know:
- What service is running?
- Does it have known vulnerabilities?
- Who can access it?

Port 631 is open on my VM, but that doesn't make it a vulnerability — it's just exposed. To exploit it, there would need to be an actual flaw in the IPP service.

## Why This Matters
Reconnaissance is the first step in any attack. Attackers scan for open ports, identify services, then research vulnerabilities.