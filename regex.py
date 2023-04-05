import re

with open("test.txt") as emails:
    emails_list = emails.read()

domain_names = set(re.findall(r'[\w\.-]+@[\w\.-]+', emails_list))
sorted_domains = sorted(domain_names)
for domain in sorted_domains:
    print(domain)
