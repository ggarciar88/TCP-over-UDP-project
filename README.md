```text
                             _           ___   ___  
                            (_)         / _ \ / _ \   not©          not©          not©          not©          not©          not©          not©          not©          not©
   __ _ __ _ __ _ _ __ ___ _ __ _ _  __| (_) | (_) |       not©          not©          not©          not©          not©          not©          not©          not©          not©    
  / _` |/ _` |/ _` | '__/ __| |/ _` |   > _ < > _ <              not©          not©          not©          not©          not©          not©          not©          not©          not©     
 | (_| | (_| | (_| | |  ( __| | (_| | || (_) | (_) |
  \__, |\__, |\__,_|_|\___|_|\__,_|_| \___/ \___/                 
   __/ | __/ |                                       
  |___/ |___/                                        
     

@ggarciar88  //  tcp_over_udp_ELITE  
____________________________________________________________________________________________________________________________________________________________________________________________________________________
# TCP over UDP – Custom Reliable Transport Protocol (TCP Reno Simulation)
____________________________________________________________________________________________________________________________________________________________________________________________________________________

This project implements a **custom reliable transport protocol over UDP**, inspired by TCP behavior and congestion control mechanisms.

It recreates key internal TCP mechanisms such as:

- Three-way handshake
- Reliable data transmission
- Timeout-based retransmission
- Congestion control (TCP Reno style)
- Slow Start
- Congestion Avoidance
- Dynamic ssthresh
- Packet loss simulation
- Congestion window evolution plotting

This is an academic-level networking project designed to demonstrate deep understanding of transport-layer protocols.

---

## Overview

Unlike standard TCP, this implementation builds reliability manually on top of UDP sockets.

It includes:

- Custom packet header
- Sequence numbers
- ACK-based reliability
- Checksum validation (SHA-256 truncated)
- Timeout retransmissions
- Simulated packet loss (20%)
- Congestion window (`cwnd`) management
- Logging of cwnd evolution
- Graphical visualization of congestion behavior

This project is ideal for demonstrating knowledge in:

- Advanced networking
- Transport layer design
- Congestion control algorithms
- Telecommunications engineering concepts

---

## Project Structure

tcp_over_udp_elite/
├── README.md
├── common.py
├── server.py
├── client.py
├── plot_cwnd.py
└── cwnd_log.txt (generated after execution)


---

## Protocol Features

###  Three-Way Handshake
Implements:
- SYN
- SYN-ACK
- ACK

###  Reliable Transmission
- Timeout detection
- Automatic retransmission
- ACK validation

###  Congestion Control (TCP Reno Inspired)

Implements:

- Slow Start (cwnd doubles)
- Congestion Avoidance (linear growth)
- ssthresh dynamic update
- Timeout → cwnd reset to 1

###  Packet Loss Simulation

Simulated loss probability:

    LOSS_PROBABILITY = 0.2

This forces congestion behavior and allows testing retransmission logic.

---

## Technologies Used

- **Python 3**
- **UDP sockets**
- **Hashlib (SHA-256 checksum)**
- **Matplotlib** (for congestion window visualization)

Compatible with Linux, macOS, and Windows (with Python installed).

---

## How to Run

###  Start Server

Open Terminal 1:

    python server.py

Server listens on:

    127.0.0.1:9002

---

###  Start Client

Open Terminal 2:

    python client.py

You will observe:

- Congestion window evolution
- Slow start phase
- Congestion avoidance
- Timeout events

---

###  Visualize Congestion Window

After execution:

    python plot_cwnd.py

This will display the cwnd growth graph.

---

## Example Output (Client)

    [CLIENT] cwnd=2, ssthresh=8
    [CLIENT] cwnd=4, ssthresh=8
    [CLIENT] cwnd=8, ssthresh=8
    [CLIENT] cwnd=9, ssthresh=8
    [CLIENT] Timeout -> Congestion detected
    [CLIENT] cwnd=1, ssthresh=4

This behavior mimics real TCP Reno congestion control dynamics.

---

## Default Configuration

- Port: 9002
- Packet loss simulation: 20%
- Timeout: 1 second
- Initial cwnd: 1
- Initial ssthresh: 8

---

## Intended Audience

This project is suitable for:

- Telecommunications Engineering students
- Networking specialization students
- Engineers preparing for networking interviews
- Anyone studying transport-layer protocol design
- Developers interested in understanding how TCP works internally

---

## Why This Project Matters

Most developers use TCP without understanding:

- How congestion control works
- How retransmission is handled
- How cwnd evolves
- Why packet loss affects throughput

This project demonstrates those mechanisms explicitly and programmatically.

It goes beyond socket usage — it explores protocol engineering.

---

## Future Improvements

- RTT estimation (Jacobson/Karels algorithm)
- Fast retransmit (3 duplicate ACKs)
- Selective acknowledgements (SACK)
- Multi-client support
- Docker containerization
- Automated testing suite

---

## License

Open-source and free for academic and educational use.

MIT License.
