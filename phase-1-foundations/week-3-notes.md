# Week 3: Wireshark & Packet Analysis

## What is Wireshark?
Wireshark is a network packet analyser tool that lets you see all the packets moving in and out of your network in real time. It's like a security camera for your network traffic.

With Wireshark, you can:
- See the TCP three-way handshake happening live
- Capture DNS queries (when your computer asks for an IP address)
- Capture DNS responses (when a DNS server gives back the IP)
- View the source and destination IP addresses of every request
- Identify what websites/services are being accessed

## How It Works (Example)
When I typed google.com in the browser while capturing packets:
1. The browser sent a DNS query asking "What's the IP address for www.google.com?"
2. The DNS server responded with the IP address (142.251.150.x)
3. The browser then used that IP to fetch the actual webpage

I saw all three of these steps happen in real time in Wireshark.

## Why This Matters for Cybersecurity
With Wireshark, you can spot suspicious network activity — like unexpected connections, data being sent to unknown servers, or malicious traffic. It's your first tool for network investigation.