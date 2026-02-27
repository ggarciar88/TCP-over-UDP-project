
import socket
from common import *

SERVER_ADDR = ("0.0.0.0", 9002)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(SERVER_ADDR)

print("[SERVER] Esperando conexión...")

expected_seq = 1
server_seq = 5000

while True:
    data, addr = sock.recvfrom(4096)
    if simulate_packet_loss():
        print("[SERVER] Paquete perdido (simulado)")
        continue

    seq, ack, flags, window, timestamp, payload = parse_packet(data)

    if flags & FLAG_SYN:
        syn_ack = build_packet(server_seq, seq + 1, FLAG_SYN | FLAG_ACK, 10)
        sock.sendto(syn_ack, addr)

    elif flags & FLAG_DATA:
        if seq == expected_seq:
            print("[SERVER] Datos:", payload.decode())
            expected_seq += len(payload)
        ack_pkt = build_packet(server_seq, expected_seq, FLAG_ACK, 10)
        sock.sendto(ack_pkt, addr)

    elif flags & FLAG_FIN:
        fin_ack = build_packet(server_seq, seq + 1, FLAG_ACK | FLAG_FIN, 10)
        sock.sendto(fin_ack, addr)
        break
