import urllib3
import random
from concurrent.futures import ThreadPoolExecutor
from faker import Faker

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

def main():
    domain = input("Enter the domain (e.g., https://example.com): ")
    num_requests = int(input("How many requests would you like to send? "))
    origin = domain
    referer = domain
    with ThreadPoolExecutor(max_workers=100) as executor:
        for _ in range(num_requests):
            executor.submit(send_request, domain, origin, referer)

if __name__ == "__main__":
    main()
