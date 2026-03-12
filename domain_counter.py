
# basically the function needs to parse the domain counts and add up the count for each domain and for each subdomain i.e.
# Input: url counts "100 apps.google.com,200 calendar.google.com,50 my.pony.com"
# Output "100 apps.google.com,200 calendar.google.com,50 my.pony.com,300 google.com,50 pony.com,350 com"


import sys


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


if __name__ == "__main__":
    print(calculate_count_domains("100 apps.google.com,200 calendar.google.com,50 my.pony.com"))
