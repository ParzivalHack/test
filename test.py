import subprocess

def capture_traffic(interface):
    try:
        # Run tshark command to capture traffic on the specified interface
        command = f"tshark -i {interface} -T fields -e ip.src -e ip.dst -e ip.proto"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = process.communicate()

        # Process the captured packet information
        packets = stdout.decode().splitlines()
        for packet in packets:
            src_ip, dst_ip, protocol = packet.split("\t")
            print(f"Source IP: {src_ip}")
            print(f"Destination IP: {dst_ip}")
            print(f"Protocol: {protocol}")
            print()

    except FileNotFoundError:
        print("Wireshark package not found. Please install Wireshark in Termux.")

def main():
    print("CyberTrace - Network Traffic Analyzer")
    print("------------------------------------")

    # Get user input for interface
    interface = input("Enter the network interface to capture traffic from: ")

    print("\nPress Ctrl+C to stop capturing traffic.\n")

    capture_traffic(interface)

if __name__ == "__main__":
    main()
