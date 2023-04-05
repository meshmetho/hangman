name = "Mesh"
print(name)

age = 22
print(age)

height = 179.5
print(height)
print("Mesh is \nthe best")
a = "Mesh is the best"
b = a.upper()
print(b)
name = "Meshack Metho"
print(name.find("M"))
Mesh = {"age": 22, "school": "jkuat", "height": 179.5}
Mesh["school"] = "Zindua school"
Mesh["complexion"] = "dark"
print(Mesh)



import re

# Open the file containing the email addresses
with open('test.txt', 'r') as f:
    email_list = f.read()

# Extract domain names using regular expressions
domain_names = set(re.findall(r'[\w\.-]+@[\w\.-]+', email_list))
# Sort domain names alphabetically
sorted_domains = sorted(domain_names)

# Output the sorted domain names
for domain in sorted_domains:
    print(domain)
