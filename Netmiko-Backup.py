
# Radoslaw Gorski - Python for Network Automation
# Netmiko + Napalm example - used at Three Ireland

from netmiko import ConnectHandler
from datetime import datetime
import difflib

# Example device list - like Mars EMEA 100+ sites
DEVICES = [
    {"device_type": "cisco_nxos", "host": "10.10.1.10", "username": "admin", "password": "lab", "name": "LEAF-01"},
    {"device_type": "juniper_junos", "host": "10.10.1.20", "username": "admin", "password": "lab", "name": "MX-01"},
]

def backup_and_check(device):
    print(f"\n=== {device['name']} ({device['host']}) ===")
    try:
        conn = ConnectHandler(**device)
        # Pre-check
        bgp = conn.send_command("show ip bgp summary" if "cisco" in device["device_type"] else "show bgp summary")
        print(f"BGP Pre: {bgp[:200]}...")
        
        # Backup
        config = conn.send_command("show running-config" if "cisco" in device["device_type"] else "show configuration")
        filename = f"backups/{device['name']}-{datetime.now().isoformat()}.cfg"
        open(filename, 'w').write(config)
        print(f"Backup saved: {filename}")
        
        # Compliance: check NTP present
        if "ntp server" not in config:
            print("COMPLIANCE FAIL: NTP missing")
        else:
            print("COMPLIANCE PASS")
        
        conn.disconnect()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    for dev in DEVICES:
        backup_and_check(dev)
