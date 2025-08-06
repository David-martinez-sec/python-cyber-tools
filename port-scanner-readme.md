# 🔎 Python Port Scanner

This is a simple Python-based port scanner I created as part of my journey into cybersecurity and Python scripting. It scans TCP ports on a given host and reports which ones are open — offering insight into exposed network services and potential attack surfaces.

---

## 💡 Project Purpose

The goal of this project is to understand:

- How port scanning works at a low level
- What open ports reveal about a system
- How Python can be used for basic network recon

This scanner uses Python’s built-in `socket` library to attempt TCP connections to common ports (1–1024) on a target IP or hostname. If a connection succeeds, the port is reported as open, along with its typical service name (e.g., SSH, DNS).

---

## 🌐 Understanding Ports

In networking, a **port** is a virtual gate through which data enters or leaves a computer. Each port number corresponds to a specific type of service or application.

### Common TCP Ports and Services

| Port | Service | Use |
|------|---------|-----|
| 22   | SSH     | Secure remote login to systems (commonly used by sysadmins) |
| 53   | DNS     | Domain name resolution (translates URLs to IP addresses) |
| 80   | HTTP    | Unencrypted web traffic |
| 443  | HTTPS   | Secure/encrypted web traffic |
| 88   | Kerberos | Authentication protocol used in enterprise environments |
| 445  | SMB     | Windows file sharing and network browsing |

Open ports typically mean that a service is **listening** and ready to accept connections.

---

## 🛡️ Why This Matters in Cybersecurity

Scanning for open ports is one of the first steps in:
- Reconnaissance during penetration testing
- Asset discovery in blue team security
- Identifying vulnerable services or misconfigured systems

An open port doesn’t mean vulnerability — but it does mean **exposure**. That’s why understanding **which ports are open** and **why** is critical to any security posture.

---

## 🧠 Key Python Concepts Used

While the script itself is minimal, it uses foundational Python concepts including:
- `socket.socket()` to initiate network connections
- `connect_ex()` to check if a port is open
- `getservbyport()` to identify common services
- Looping, timeouts, and error handling for clean output

This was edited and updated directly in the terminal using `nano`, reinforcing both scripting and shell fluency.

---

## ⚠️ Ethical Use Only

This tool is intended for **learning and self-assessment only**. Port scanning systems you do not own or have explicit permission to scan may be illegal and is not advised.

---

## 🔜 Next Steps

Improvements I plan to explore:
- Multi-threaded scanning for speed
- Custom port range input
- Banner grabbing for deeper service info
- Exporting results to file
- Integration with other tools (e.g., Nmap)

---

## ✍️ Final Thoughts

This project helped solidify my understanding of:
- How systems expose services through ports
- The link between network visibility and security
- Using Python for practical, real-world tasks

It’s a small step in building a practical cybersecurity toolkit.

