from scapy.all import ARP, Ether, srp
import socket
import ipaddress
import json
import os
from datetime import datetime
import time
import sys

KNOWN_FILE = "known_devices.json"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def log_scan(devices):
    with open("scan.log", "a") as f:
        f.write(f"\nScan Time: {datetime.now()}\n")
        for d in devices:
            f.write(f"{d['ip']} {d['mac']} {d['hostname']} {d['status']}\n")


def get_network_range(ip):
    network_var = ipaddress.ip_network(ip + "/24", strict=False)
    return str(network_var)

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

def arp_scan(network_var):
    arp = ARP(pdst=network_var)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []

    for sent, recived in result:
        devices.append({
            "ip": recived.psrc,
            "mac": recived.hwsrc,
            "hostname": get_hostname(recived.psrc)
        })
        return devices

def monitor_network(interval=30):
    print("\nMonitoring network for new devices...\n")
    known_devices = load_known_devices()

    while True:
        devices = arp_scan(get_network_range(get_local_ip()))

        for d in devices:
            if d["mac"] not in known_devices:
                print(f"🚨 NEW DEVICE DETECTED: {d['ip']} {d['mac']}")
                known_devices[d["mac"]] = {
                    "ip": d["ip"],
                    "hostname": d["hostname"]
                }
                save_known_devices(known_devices)

        time.sleep(interval)


def load_known_devices():
    if not os.path.exists(KNOWN_FILE):
        return {}
    with open(KNOWN_FILE,"r") as f:
        return json.load(f)

def save_known_devices(devices):
    with open(KNOWN_FILE,"w") as f:
        json.dump(devices,f, indent=4)

def print_table(devices):
    log_scan(scanned_devices)
    print("\nIP Address      MAC Address        Hostname            Status")
    print("-" * 65)

    for d in devices:
        print(f"{d['ip']:15} {d['mac']:18} {d['hostname']:20} {d['status']}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        monitor_network()
    else:
        local_ip = get_local_ip()
        network = get_network_range(local_ip)

        known_devices = load_known_devices()
        devices = arp_scan(network)

        scanned_devices = []

        for d in devices:
            mac = d["mac"]
            if mac in known_devices:
                status = "Known"
            else:
                status = "⚠ NEW"
                known_devices[mac] = {
                    "ip": d["ip"],
                    "hostname": d["hostname"]
                }
            d["status"] = status
            scanned_devices.append(d)

        print_table(scanned_devices)
        save_known_devices(known_devices)
        log_scan(scanned_devices)



