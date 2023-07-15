import psutil
import time
from datetime import datetime
#import matplotlib.pyplot as plt

last_time = datetime.now()
last_bytes_sent = psutil.net_io_counters().bytes_sent
last_bytes_recv = psutil.net_io_counters().bytes_recv
interval = 1  # Time interval in seconds

while True:
    # Get current time and network usage
    current_time = datetime.now()
    current_bytes_sent = psutil.net_io_counters().bytes_sent
    current_bytes_recv = psutil.net_io_counters().bytes_recv

    # Calculate bandwidth
    time_diff = (current_time - last_time).total_seconds()
    bytes_sent_diff = current_bytes_sent - last_bytes_sent
    bytes_recv_diff = current_bytes_recv - last_bytes_recv
    sent_bandwidth = bytes_sent_diff / time_diff
    recv_bandwidth = bytes_recv_diff / time_diff

    # Print bandwidth information
    print(f"Sent: {sent_bandwidth:.2f} bytes/s")
    print(f"Received: {recv_bandwidth:.2f} bytes/s")

    # Update previous values
    last_time = current_time
    last_bytes_sent = current_bytes_sent
    last_bytes_recv = current_bytes_recv

    # Wait for the specified interval
    time.sleep(interval)

#for plotting data use the code below
"""Plotting the data
plt.plot(current_time, sent_bandwidth, 'r-', label='Sent')
plt.plot(current_time, recv_bandwidth, 'b-', label='Received')
plt.xlabel('Time')
plt.ylabel('Bandwidth (bytes/s)')
plt.legend()
plt.pause(interval)
plt.clf()
"""
