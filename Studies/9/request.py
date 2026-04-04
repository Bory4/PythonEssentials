import requests, threading, time

def crawl(link):
    print(f"crawl started for {link}")
    r = requests.get(link)
    if r.status_code == 200:
        print(f"crawl ended for {link}, length: {len(r.text)}")
    else:
        print("Something went wrong... Try again")

links = [
    "https://python.org",
    "https://example.com",
    "https://8.8.8.8"
]

threads = []
for link in links:
    t = threading.Thread(target=crawl, args=(link,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
