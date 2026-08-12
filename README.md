# Cybersecurity Journey 🛡️

A public log of my cybersecurity learning journey — from absolute beginner to job-ready.

Every phase produces real projects and scripts. Everything is documented here as I build it.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| 1 | Foundations (Networking, Linux, Security Basics) | ✅ Complete |
| 2 | Hands-on Hacking (Web Security, Ethical Hacking, Python) | 🚀 In Progress |
| 3 | Specialisation | 📋 Planned |
| 4 | AI + Security | 📋 Planned |

## Progress Log

| Date | Milestone | Notes |
|------|-----------|-------|
| 27/05/2026 | Repo created | Starting Phase 1 |
| 14/06/2026 | Weeks 1-5 complete | DNS/TCP-IP, Linux fundamentals, Wireshark packet analysis, Nmap reconnaissance, Python port scanner |
| 18/07/2026 | Phase 1 complete (Weeks 1-10) | Service fingerprinting, file I/O, CSV vulnerability scanner, APIs, JSON, reconnaissance tool capstone |

## Phase 1: Foundations ✅

### Week 1: How the Internet Works
- DNS queries and responses
- TCP/IP model (Application, Transport, Internet, Link layers)
- TCP three-way handshake
- DNS poisoning attack concept
- [Notes](./phase-1-foundations/week-1-notes.md)

### Week 2: Linux & File Permissions
- Terminal navigation and commands (pwd, ls, cd, touch, nano, cp)
- File permissions (rwx) and chmod
- Understanding users, groups, and others
- File system structure (/bin, /etc, /home, /var/log, etc.)
- [Notes](./phase-1-foundations/week-2-notes.md)

### Week 3: Wireshark & Packet Analysis
- Capturing live network packets
- DNS queries and responses in action
- Understanding packet structure (source IP, destination IP, ports)
- Interface selection and filtering
- [Notes](./phase-1-foundations/week-3-notes.md)

### Week 4: Nmap & Network Reconnaissance
- Network scanning with ping scans
- Port scanning and open port discovery
- Port vs vulnerability distinction
- Reconnaissance workflow
- [Notes](./phase-1-foundations/week-4-notes.md)

### Week 5: Python Port Scanner
- Sockets and two-way communication
- socket.connect_ex() for port testing
- Building security tools from scratch
- Real example: scanned Google DNS (8.8.8.8), found port 53 open
- [Code + Notes](./phase-1-foundations/week-5-notes.md)

### Week 6: Service Fingerprinting & Banners
- Banner grabbing (what services send when connected)
- Difference between connect_ex() and connect()
- recv() method for reading socket data
- Enhanced scanner with service identification
- [Notes](./phase-1-foundations/week-6-notes.md)

### Week 7: File I/O & Logging
- Reading and writing files in Python
- with statement for safe file handling
- 'w' mode (write/overwrite) vs 'a' mode (append)
- Logging scan results to files
- [Notes](./phase-1-foundations/week-7-notes.md)

### Week 8: CSV-Based Vulnerability Scanner
- Reading CSV vulnerability databases
- Searching for matching CVEs
- Building a functional security tool
- CSV parsing and data handling
- [Code + Notes](./phase-1-foundations/week-8-notes.md)

### Week 9: APIs & JSON
- Understanding JSON structure and parsing
- How REST APIs work
- Making HTTP requests with requests library
- Parsing API responses with .json()
- [Code + Notes](./phase-1-foundations/week-9-notes.md)

### Week 10: Reconnaissance Tool Capstone
- Complete end-to-end reconnaissance automation
- Port scanning + service identification + vulnerability research
- Generating security reports
- Combining all Phase 1 concepts into one working tool
- [Full Tool](./phase-1-foundations/reconnaissance_tool.py) | [Notes](./phase-1-foundations/week-10-notes.md)

## Key Projects

| Project | Description | Technologies |
|---------|-------------|---------------|
| **Port Scanner** | Python tool using sockets to discover open ports | Python, Sockets |
| **Service Identifier** | Identifies services running on open ports | Python, Socket API |
| **CSV Vulnerability Scanner** | Searches database for known CVEs | Python, CSV |
| **Reconnaissance Tool** | Complete automation: scan → identify → search → report | Python, Sockets, CSV |
| **Packet Analysis** | Wireshark captures showing real DNS/HTTP traffic | Wireshark, Ubuntu VM |

## Tech Stack

- **Languages:** Python 3, Bash
- **Tools:** Linux (Ubuntu 26.04), Wireshark, Nmap, VirtualBox
- **Platforms:** GitHub (documentation + code), GitHub Pages (portfolio)
- **Databases:** CSV (vulnerability data)

## Learning Philosophy

- **Learn by doing** — Build tools, not just watch tutorials
- **Understand every line** — No copy-paste; write and debug your own code
- **Document publicly** — LinkedIn posts + GitHub notes after every milestone
- **Active recall** — Anki flashcards to lock in concepts
- **Real targets** — Test on actual systems (8.8.8.8, localhost, etc.)

## What's Next (Phase 2)

- Web application security
- Burp Suite for intercepting/modifying traffic
- SQL injection and other web vulnerabilities
- Exploitation frameworks
- Real hacking projects

---

**Progress:** 10 weeks of Phase 1 complete. Real tools built. Ready for deeper hacking.

Follow the journey: [LinkedIn](https://linkedin.com/in/okoroprince)