# Week 5: Python Port Scanner with Sockets

This week I built a functional port scanner in Python using sockets — my first hands-on security tool.

## What is a Socket?

A socket is a two-way communication channel between two devices over a network. It's the underlying mechanism that allows one computer to reach out and test if another computer is listening on a specific port and IP address.

## Understanding connect_ex()

`connect_ex()` is a socket method that attempts to connect to a target IP and port. It returns:
- **0** if the connection succeeds (port is open)
- **11 or 111** if the connection is refused (port is closed) — the exact code depends on the operating system

## Building the Port Scanner

I wrote a Python program that:
1. Takes a target IP address from the user
2. Takes a port range (start and end port)
3. Loops through each port in that range
4. Attempts to connect to each port using `connect_ex()`
5. Reports which ports are open

**The Code:**

```python
import socket

def scan_port(ip, port):
    try:
        target = (ip, port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(target)
        sock.close()
        return result == 0
    except Exception as e:
        return False

def main():
    print("==Welcome==")
    host = input("Enter the host address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    for port in range(start_port, end_port + 1):
        result = scan_port(host, port)
        if result == True:
            print(f"Port {port} is OPEN on {host}")

if __name__ == "__main__":
    main()
```

## Real Example

I scanned Google's public DNS server (8.8.8.8) on ports 50-60 and found **port 53 open** — which is DNS, Google's nameserver.

## Why This Matters

This is reconnaissance — the first step attackers take:
1. **Scan for open ports** (what I just did)
2. **Identify services** running on those ports
3. **Research vulnerabilities** in those services
4. **Exploit** if vulnerabilities exist

Open ports are entry points. By learning to scan like an attacker, I understand how to think defensively. This is foundational to cybersecurity.