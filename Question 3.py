# QUESTION 3

import string
# Read the file into a list of lines
file = open("sample-file.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

duplicates_dict = {}

for index, original_line in enumerate(lines):
    line_num = index + 1

    if not original_line.strip():
        continue

    # Clean the line
    normalized = original_line.lower()
    clean_line = ""
    for char in normalized:
        if char not in string.punctuation and not char.isspace():
            clean_line += char

    # Add to dictionary
    if clean_line not in duplicates_dict:
        duplicates_dict[clean_line] = []

    duplicates_dict[clean_line].append((line_num, original_line.strip()))

# Find sets that have more than 1 line
near_duplicate_sets = []
for key in duplicates_dict:
    if len(duplicates_dict[key]) > 1:
        near_duplicate_sets.append(duplicates_dict[key])

# Print the number of sets found
print(f"Number of near-duplicate sets: {len(near_duplicate_sets)}")
print("-" * 30)

# Print the first two sets found
for i in range(min(2, len(near_duplicate_sets))):
    print(f"Set {i + 1}:")
    for line_num, original in near_duplicate_sets[i]:
        print(f"{line_num}: {original}")
    print()
