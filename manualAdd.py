###########################################################
# Script to input domains, load existing domains from file,
# append user domains, and sort the file
###########################################################

file_path = "merged_block.txt"
domains_set = set()
origin_len = 0

# Load existing domains from file into a set
try:
    with open(file_path, "r") as file:
        existing_domains = file.read().splitlines()
        domains_set.update(existing_domains)
        origin_len = len(domains_set)
except FileNotFoundError:
    # If the file doesn't exist yet, create an empty set
    existing_domains = []

print("Enter domains one by one. Type 'done' when finished.")

while True:
    domain = input("Enter a domain (or 'done' to finish): ").strip()

    if domain.lower() == "done":
        break
    elif domain:
        domains_set.add(domain)

# Write the combined set of domains to merged_block.txt
with open(file_path, "w") as file:
    file.write("\n".join(sorted(domains_set)))

print(f"{len(domains_set)-origin_len} domains added to {file_path} and sorted.")
