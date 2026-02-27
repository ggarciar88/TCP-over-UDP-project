
import struct
import hashlib
import time
import random

HEADER_FORMAT = "!I I H H d"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

FLAG_SYN = 0x1
FLAG_ACK = 0x2
FLAG_FIN = 0x4
FLAG_DATA = 0x8

MAX_PAYLOAD = 1024
TIMEOUT = 1.0
LOSS_PROBABILITY = 0.2  # Simulated packet loss (20%)

def checksum(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()[:8]

def build_packet(seq, ack, flags, window, payload=b""):
    timestamp = time.time()
    header = struct.pack(HEADER_FORMAT, seq, ack, flags, window, timestamp)
    chksum = checksum(header + payload)
    return header + chksum + payload

def parse_packet(packet: bytes):
    header = packet[:HEADER_SIZE]
    chksum = packet[HEADER_SIZE:HEADER_SIZE+8]
    payload = packet[HEADER_SIZE+8:]

    if checksum(header + payload) != chksum:
        raise ValueError("Checksum inválido")

    seq, ack, flags, window, timestamp = struct.unpack(HEADER_FORMAT, header)
    return seq, ack, flags, window, timestamp, payload

def simulate_packet_loss():
    return random.random() < LOSS_PROBABILITY
