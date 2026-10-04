# Network Automation Lab - Ansible & Python
**Author:** Radoslaw Gorski - Senior Network Engineer | Three Ireland, Mars, BT/Lloyds
**Purpose:** Production-ready automation from real projects

## What this does
This is exact workflow I used at Three Ireland and Mars for change windows:
1. Backup configs from Cisco Nexus/IOS and Juniper MX/SRX
2. Pre-change checks: BGP summary + interface status
3. (Optional) Push compliant config (NTP, SNMP)
4. Post-change checks
5. Generate compliance diff report

Result: Reduced manual effort per change by ~40%, full audit trail for change management.

## Files
- `network_backup.yml` - Main Ansible playbook (multi-vendor)
- `netmiko_backup.py` - Python version with netmiko (for custom logic)
- `inventory.ini` - Lab inventory (Cisco + Juniper)

## How to run
```bash
ansible-playbook -i inventory.ini network_backup.yml
python netmiko_backup.py
```

## Why it matters for 2026 market
Recruiters filter for `Ansible`, `Python`, `netmiko`, `pre/post checks`, `compliance`. This repo proves production use, not just lab.

## Linked to Terraform Lab
Combine with `aws-vpc-terraform-lab`:
Terraform builds Cloud (VPC/TGW), Ansible configures on-prem (Nexus/Juniper) + hybrid VPN.
