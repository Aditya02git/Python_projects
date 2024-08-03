import socket
import sys

def get_interface():
    if len(sys.argv) != 2:
        print("Usage: python script.py <interface>")
        sys.exit(1)
    return sys.argv[1]

def sniff(iface):
    # Create a UDP socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((iface, 0))
    except socket.error as e:
        print(f"Error creating socket: {e}")
        sys.exit(1)

    while True:
        packet, _ = sock.recvfrom(65535)
        process_packet(packet)

def process_packet(packet):
    # This is a simplified packet handler for demo purposes.
    print(f"Received packet: {packet}")

# Get the network interface from the command line arguments and start sniffing
iface = get_interface()
sniff(iface)
