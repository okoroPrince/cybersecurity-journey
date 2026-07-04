# Week 6: Service Fingerprinting & Banner Grabbing

## What Are Banners?

Banners are identifying information that services send when you connect to them. They're like fingerprints — each service leaves its mark. Connect to port 22, you get "SSH-2.0-OpenSSH". Connect to port 80, you get "HTTP/1.1". These tell you exactly what's running.

## connect_ex() vs connect()

**connect_ex()** — Tests if a connection is possible. Returns 0 if successful, non-zero if fails. Doesn't create a real connection.

**connect()** — Actually establishes a real connection. Throws an error if it fails, so you wrap it in try-except. This is what you need to read data from.

Think of it: `connect_ex()` is knocking on the door. `connect()` is walking through it.

## recv()

`recv()` reads incoming data from an open socket. It grabs the banner the service sends back. Works only after `connect()` has established a real connection.

## Updated Port Scanner

My scanner now:
1. Scans an IP for open ports
2. Identifies what service is running on each port
3. Attempts to grab banners (where applicable)
4. Logs results

**Example:** Scanned 8.8.8.8 (Google DNS), found port 53 open with DNS service running.

## Why This Matters

Attackers follow this chain:
1. **Reconnaissance** — Scan for open ports
2. **Fingerprinting** — Identify services
3. **Research** — Find vulnerabilities in those services
4. **Exploit** — Attack the weakness

Understanding the attacker's mindset is how you defend.