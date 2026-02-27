
import matplotlib.pyplot as plt

with open("cwnd_log.txt") as f:
    data = [int(line.strip()) for line in f]

plt.plot(data)
plt.xlabel("Transmission Round")
plt.ylabel("Congestion Window (cwnd)")
plt.title("TCP Reno Congestion Window Evolution")
plt.show()
