import argparse
import curses
from scapy.all import *

def packet_handler(packet, stdscr):
    # Extract basic packet information
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    protocol = packet[IP].proto

    # Print packet details
    stdscr.addstr(f"Source IP: {src_ip}\n")
    stdscr.addstr(f"Destination IP: {dst_ip}\n")
    stdscr.addstr(f"Protocol: {protocol}\n")
    stdscr.refresh()

def capture_traffic(interface, stdscr):
    try:
        sniff(iface=interface, prn=lambda packet: packet_handler(packet, stdscr))
    except PermissionError:
        stdscr.addstr("Insufficient permissions to capture network traffic.\n")
        stdscr.refresh()
    except KeyboardInterrupt:
        stdscr.addstr("Traffic capture stopped by user.\n")
        stdscr.refresh()

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("CyberTrace - Network Traffic Analyzer\n")
    stdscr.addstr("------------------------------------\n")

    # Get user input for interface
    stdscr.addstr("Enter the network interface to capture traffic from: ")
    stdscr.refresh()
    interface = stdscr.getstr().decode()

    stdscr.addstr("\nPress 'q' to stop capturing traffic.\n\n")
    stdscr.refresh()

    capture_traffic(interface, stdscr)

def run_wizard():
    curses.wrapper(main)

if __name__ == "__main__":
    run_wizard()
