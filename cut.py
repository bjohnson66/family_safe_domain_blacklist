import re

block2_file = "block2.txt"
origin_file = "block.txt"
final_output_file = "merged_block.txt"

# Create a set to store unique lines from block.txt
unique_lines_origin = set()

# Read the original file and store unique lines in the set
with open(origin_file, "r") as origin_file:
    for line in origin_file:
        unique_lines_origin.add(line)

# Open the output file and write unique lines from block.txt
with open(final_output_file, "w") as output_file:
    for unique_line_origin in unique_lines_origin:
        output_file.write(unique_line_origin)

# Process block2.txt and merge with the final output file
with open(block2_file, "r") as block2_file, open(final_output_file, "a") as output_file:
    for line in block2_file:
        # Use regex to remove 'www.' only if it exists at the beginning of the line
        new_line = re.sub(r'^www\.', '', line)

        # Remove the first 8 characters
        new_line = new_line[8:]

        # Write the formatted line to the final output file
        output_file.write(new_line)

# Remove duplicate entries from the merged block list
unique_lines_merged = set()

with open(final_output_file, "r") as merged_file:
    for line in merged_file:
        unique_lines_merged.add(line)

# Write the final result to the merged block file
with open(final_output_file, "w") as merged_output_file:
    for unique_line_merged in unique_lines_merged:
        merged_output_file.write(unique_line_merged)
