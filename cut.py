###########################################################
#Called cut.py only because of the regex cutting off "www."
# and other garbage. Ultimately, this file takes two block lists
# and combines them into one.
###########################################################
import re

new_domains = "output_domains.txt"
origin_file = "merged_block.txt"
final_output_file = "merged_block2.txt"

# Create a set to store unique lines from both origin file and new domains
unique_lines_combined = set()
originSize = 0

# Read the original file and store unique lines in the set
with open(origin_file, "r") as origin_file:
    for line in origin_file:
        unique_lines_combined.add(line)

originSize = len(unique_lines_combined)

# Process block2.txt and store unique lines in the set
with open(new_domains, "r") as block2_file:
    for line in block2_file:
        # Use regex to remove 'www.' only if it exists at the beginning of the line
        new_line = re.sub(r'^www\.', '', line)

        # Remove the first 8 characters
        new_line = new_line[8:]

        # Add the formatted line to the set
        unique_lines_combined.add(new_line)

finalSize = len(unique_lines_combined)

# Open the output file and write unique lines from both origin and new domains
with open(final_output_file, "w") as output_file:
    for unique_line_combined in sorted(unique_lines_combined):
        output_file.write(unique_line_combined)

print(f"Added {finalSize-originSize} domains to list")