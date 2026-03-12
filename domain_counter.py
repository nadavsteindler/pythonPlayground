
# basically the function needs to parse the domain counts and add up the count for each domain and for each subdomain i.e.
# Input: url counts "100 apps.google.com,200 calendar.google.com,50 my.pony.com"
# Output "100 apps.google.com,200 calendar.google.com,50 my.pony.com,300 google.com,50 pony.com,350 com"


import time
from threading import Thread, Lock


def calculate_count_domains(arg: str) -> str:
    count_domains = arg.split(",")
    counts = {}
    for count_domain in count_domains:
        print("starting "+count_domain)
        tokens = count_domain.split(" ")
        count = int(tokens[0])
        domain = tokens[1]
        while True:
            counts[domain]=counts.get(domain, 0)+count
            pos = domain.find(".")
            if pos != -1:
                domain=domain[pos+1:]
            else:
                break

    return ",".join(f"{v} {k}" for k, v in counts.items())

def calculate_count_domains_multithread(arg: str) -> str:
    count_domains = arg.split(",")
    counts = {}
    lock = Lock()

    def process_count_domain(count_domain:str):
        print("starting "+count_domain)
        time.sleep(3)
        tokens = count_domain.split(" ")
        count = int(tokens[0])
        domain = tokens[1]
        while True:
            with lock:
                counts[domain]=counts.get(domain, 0)+count
            pos = domain.find(".")
            if pos != -1:
                domain=domain[pos+1:]
            else:
                break

    threads=[Thread(target=process_count_domain,args=(cd,)) for cd in count_domains]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return ",".join(f"{v} {k}" for k, v in counts.items())

if __name__ == "__main__":
    # print(calculate_count_domains("100 apps.google.com,200 calendar.google.com,50 my.pony.com"))
    print(calculate_count_domains_multithread("100 apps.google.com,200 calendar.google.com,50 my.pony.com"))
