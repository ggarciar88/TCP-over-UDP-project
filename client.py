
import socket
import time
from common import *

SERVER_ADDR = ("127.0.0.1", 9002)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

client_seq = 1
cwnd = 1
ssthresh = 8
cwnd_log = []

def reliable_send(packet):
    global cwnd, ssthresh
    while True:
        sock.sendto(packet, SERVER_ADDR)
        try:
            data, _ = sock.recvfrom(4096)
            return parse_packet(data)
        except socket.timeout:
            print("[CLIENT] Timeout -> Congestion detected")
            ssthresh = max(cwnd // 2, 1)
            cwnd = 1

# Handshake
syn = build_packet(client_seq, 0, FLAG_SYN, 10)
seq, ack, flags, window, timestamp, payload = reliable_send(syn)

ack_pkt = build_packet(client_seq + 1, seq + 1, FLAG_ACK, 10)
sock.sendto(ack_pkt, SERVER_ADDR)

messages = ["Pkt1", "Pkt2", "Pkt3", "Pkt4", "Pkt5", "Pkt6"]
next_seq = client_seq

for msg in messages:
    payload = msg.encode()
    pkt = build_packet(next_seq, 0, FLAG_DATA, 10, payload)
    seq_ack, ack_ack, flags_ack, window_ack, ts_ack, pl_ack = reliable_send(pkt)

    # TCP Reno-like behavior
    if cwnd < ssthresh:
        cwnd *= 2  # Slow start
    else:
        cwnd += 1  # Congestion avoidance

    cwnd_log.append(cwnd)
    print(f"[CLIENT] cwnd={cwnd}, ssthresh={ssthresh}")

    next_seq += len(payload)

# Close
fin = build_packet(next_seq, 0, FLAG_FIN, 10)
reliable_send(fin)

# Save cwnd evolution
with open("cwnd_log.txt", "w") as f:
    for value in cwnd_log:
        f.write(str(value) + "\n")

print("[CLIENT] Conexión cerrada")
