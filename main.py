"""
Network Device Ping & Report – starter scaffold

Follow the numbered TODOs in order. After each small change, run:
    python3 main.py

Milestones:
  M1: Print targets read from ips.txt
  M2: Resolve hostnames to IPs
  M3: Build the OS-specific ping command (no execution yet)
  M4: Execute ping and capture output
  M5: Parse loss/latency
  M6: Print a simple table
  M7: Write CSV to output/

NOTE: You'll also create a new file 'ping_utils.py' in the same folder for step M3+.
"""

from __future__ import annotations

import os
import csv
from datetime import datetime
from typing import List, Dict, Any, Optional

# === CONFIG ===
INPUT_FILE = "ips.txt"
OUTPUT_DIR = "output"
PING_COUNT = 4
PING_TIMEOUT_S = 3


# ========== TODO-1 (M1): Read targets from ips.txt ==========
def read_targets(path: str) -> List[str]:
    """
    Return a list of non-empty, non-comment lines from the file.
    """
    targets: List[str] = []
    with open(path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                continue
            targets.append(stripped)
        return targets

    # TODO-1a: open the file and iterate line by line
    # TODO-1b: strip whitespace; skip blanks and lines starting with '#'
    # TODO-1c: append to targets


# ========== TODO-2 (M2): Resolve hostname to IP ==========
def resolve_ip(host: str) -> Optional[str]:
    """
    Return the first resolved IPv4 address for a hostname, or None on failure.
    """
    # HINT: use socket.gethostbyname_ex(host)
    # and wrap in try/except
    # TODO-2: implement resolution and return the IP string, else None

    import socket
    import ipaddress

    try:
       
        try:
            addr = ipaddress.ip_address(host)
            if addr.version == 4: # checks for ipv4
                return host    
        except ValueError:
            pass

        sock = socket.gethostbyname_ex(host)
        ip_list = sock[2]

        if ip_list: # cheks is ip_list is atleast true meaning has atleast one val
            first_ip = ip_list[0]
            return first_ip
        else:
            return None
        
    except socket.gaierror: # gaierror is u sed to catch any DNS resolution errors specifically
        return None
    except Exception: # catches any errors
        return None
    

#Helper
def detect_os():    
    import platform

    os_name = platform.system().strip().lower()

    if "windows" in os_name:
        return "windows"
    else:
        return "unix"

    


# ========== TODO-3 (M3): Build ping command (move logic into ping_utils.py) ==========
def build_ping_command(host: str, count: int, timeout_s: int) -> tuple[list[str], str]:
    # HINT: In ping_utils.py you'll detect OS via platform.system()
    # Windows uses: -n {count}, -w {timeout_ms}
    # macOS/Linux use: -c {count}, -W {timeout_s} (Linux) or similar
    # TODO-3: return a basic Unix-style command now; replace later once ping_utils.py exists.
    flavor = detect_os()

    if flavor == "windows":
        # count = 4
        timeout_ms = timeout_s * 1000
        cmd = ["ping", "-n", str(count), "-w", str(timeout_ms), host]
        
    else:
        # count = 4
        cmd = ["ping", "-c", str(count), "-W", str(timeout_s), host]

    return (cmd, flavor)


# ========== TODO-4 (M4): Execute ping ==========
def run_command(cmd: list[str], overall_timeout_s: int) -> tuple[int, str]:
    import subprocess
    try:
        # TODO-4: use subprocess.run(..., capture_output=True, text=True, timeout=overall_timeout_s)
        # Combine stdout and stderr and return returncode + text
        if not isinstance(cmd, list):
            return 126, "BAD_CMD_TYPE"
    
  
        if not all(isinstance(item, str) for item in cmd):
            return 126, "BAD_CMD_ELEM"
        

        result =  subprocess.run(cmd, capture_output=True, text=True, timeout=overall_timeout_s)

       #temp prints
        # print(f"RC: {result.returncode}")
        # print(f"STDOUT first 200 {result.stdout[:200]}")
        # print(f"STDERR first 200 {result.stderr[:200]}")

        
        combined_output = (result.stdout or "") + "\n" + (result.stderr or "")

        return result.returncode, combined_output.strip()
    
    except FileNotFoundError: # guard for missing ping
        return 127, "PING_NOT_FOUND"
    
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"


# ========== TODO-5 (M5): Parse ping output ==========
def parse_ping_output(text: str, flavor: str) -> Dict[str, Any]:

    # HINT (Unix): look for lines like:
    #   '4 packets transmitted, 4 received, 0% packet loss'
    #   'round-trip min/avg/max/stddev = 12.3/21.5/30.7/3.2 ms'
    # HINT (Windows): look for:
    #   'Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)'
    #   'Minimum = 10ms, Maximum = 30ms, Average = 20ms'

    import re

    UNIX_PACKETS_PATTERN = r"(\d+)\s+packets transmitted,\s+(\d+)\s+received.*?(\d+)%\s+packet loss"
    UNIX_RTT_PATTERN = r"=\s*([0-9.]+)/([0-9.]+)/([0-9.]+)/([0-9.]+)\s*ms"

    WINDOWS_PACKETS_PATTERN = r"Sent\s*=\s*(\d+),\s*Received\s*=\s*(\d+),\s*Lost\s*=\s*\d+\s*\((\d+)%\s*loss\)"
    WINDOWS_TIMES_PATTERN = r"Minimum\s*=\s*(\d+)ms,\s*Maximum\s*=\s*(\d+)ms,\s*Average\s*=\s*(\d+)ms"

    result = {
        "packets_sent": None,
        "packets_received": None,
        "packet_loss_pct": None,
        "min_ms": None,
        "avg_ms": None,
        "max_ms": None,
    }

    text = (text or "").strip()
    #TEMP
    #print(f"Ping Output: {text}")

    if flavor == "windows":
        msg = re.search(WINDOWS_PACKETS_PATTERN, text, flags=re.I)
        if msg:
            result["packets_sent"] = int(msg.group(1))
            result["packets_received"] = int(msg.group(2))
            result["packet_loss_pct"] = float(msg.group(3))
        
        msg2 = re.search(WINDOWS_TIMES_PATTERN, text, flags=re.I)
        if msg2:
            result["min_ms"] = float(msg2.group(1))
            result["max_ms"] = float(msg2.group(2))
            result["avg_ms"] = float(msg2.group(3))
            

    else:
        msg = re.search(UNIX_PACKETS_PATTERN, text)
        if msg:
            result["packets_sent"] = int(msg.group(1))
            result["packets_received"] = int(msg.group(2))
            result["packet_loss_pct"] = float(msg.group(3))
        
        msg2 = re.search(UNIX_RTT_PATTERN, text)
        if msg2:
            result["min_ms"] = float(msg2.group(1))
            result["avg_ms"] = float(msg2.group(2))
            result["max_ms"] = float(msg2.group(3))

    return result



# ========== TODO-6 (M6): Print a simple table ==========
def print_row(host: str, ip: Optional[str], reachable: bool, loss: Optional[float], avg: Optional[float]) -> None:
    loss_s = "-" if loss is None else f"{loss:.1f}"
    avg_s = "-" if avg is None else f"{avg:.1f}"
    print(f"{host:<22} {str(reachable):<9} {loss_s:<6} {avg_s:<7} {ip or '-'}")


# ========== TODO-7 (M7): Write CSV ==========
def write_csv(rows: List[Dict[str, Any]], out_dir: str) -> str:
    
 # TODO-7: write rows as CSV using csv.DictWriter

    os.makedirs(out_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_path = os.path.join(out_dir, f"report_{ts}.csv")
   
    field_names = [
        "timestamp",
        "host",
        "resolved_ip",
        "reachable",
        "packets_sent",
        "packets_received",
        "packet_loss_pct",
        "avg_ms",
        "min_ms",
        "max_ms",
    ]
    with open(out_path, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()

        for row in rows:

            copy_of_row = row.copy() # copy of row so we dont mess original row in memory

            for key in ("packet_loss_pct", "avg_ms", "min_ms", "max_ms"):
                if copy_of_row[key] is None:
                    copy_of_row[key] = ""
            writer.writerow(copy_of_row)
        
    return out_path


def main() -> None:
    # --- Milestone M1: just read and print targets ---
    targets = read_targets(INPUT_FILE)
    if not targets:
        print(f"No targets found in {INPUT_FILE}. Add some hosts (e.g., 8.8.8.8, google.com).")
        return

    print("Ping Report (starter)")
    print("-" * 80)
    print(f"{'Host':<22} {'Reachable':<9} {'Loss%':<6} {'Avg':<7} IP")
    print("-" * 80)

    # For now, we'll do a single-pass, sequential loop. Concurrency is a later stretch goal.
    rows: List[Dict[str, Any]] = []
    for host in targets:
        ip = resolve_ip(host)  # M2
        cmd, flavor = build_ping_command(host, PING_COUNT, PING_TIMEOUT_S)
        rc, out = run_command(cmd, overall_timeout_s=PING_TIMEOUT_S * (PING_COUNT + 1))
        metrics = parse_ping_output(out, flavor)
        #TEMP
        # print("PARSED:", metrics)

        reachable = ((metrics["packet_loss_pct"] is not None and metrics["packet_loss_pct"] < 100.0) or (metrics["packets_received"] is not None and metrics["packets_received"] > 0))

        print_row(
            host=host,
            ip=ip,
            reachable=reachable,
            loss=metrics["packet_loss_pct"],
            avg=metrics["avg_ms"],
        )

        rows.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "host": host,
            "resolved_ip": ip or "",
            "reachable": reachable,
            "packets_sent": metrics["packets_sent"],
            "packets_received": metrics["packets_received"],
            "packet_loss_pct": metrics["packet_loss_pct"],
            "avg_ms": metrics["avg_ms"],
            "min_ms": metrics["min_ms"],
            "max_ms": metrics["max_ms"],
        })

    # M7: write CSV (implement write_csv later)
    out_path = write_csv(rows, OUTPUT_DIR)
    print("-" * 80)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()