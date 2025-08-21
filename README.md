# Network Device Ping & Report Project

A lightweight Python utility that automates ping checks across a list of hosts/domains and generates both terminal output and CSV reports for later analysis.  
This is useful for quickly testing network availability, DNS resolution, and latency across multiple devices or domains.

---

## Features
- Read a list of targets (IPs/domains) from `ips.txt`.
- Detects your platform (macOS/Unix or Windows) and uses the correct ping command.
- Runs each ping with timeout safeguards to avoid hanging.
- Parses ping output to extract:
  - Packets sent, received, and % loss
  - Min, Avg, Max round-trip times (ms)
- Prints results in a formatted table in the terminal.
- Exports results to a timestamped CSV file under `output/`.

---

## Example Usage
1. Add IPs or domains to `ips.txt` (one per line).
2. Run:
   ```bash
   python3 main.py
