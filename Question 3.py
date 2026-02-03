# QUESTION 3
#FIX IT NOT DONE YET

import string

# QUESTION 3
# 1. Read the file into a list of lines
file = open("sample-file.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

# Dictionary to store: {normalized_text: [(line_num, original_text), ...]}
duplicates_dict = {}

for index, original_line in enumerate(lines):
    # Get the line number (index + 1)
    line_num = index + 1

    # Clean the line: lowercase and remove whitespace/punctuation
    normalized = original_line.lower()

    # Remove punctuation and whitespace
    # We can use a loop or .replace() / .translate()
    clean_line = ""
    for char in normalized:
        if char not in string.punctuation and not char.isspace():
            clean_line += char

    # Add to dictionary
    if clean_line not in duplicates_dict:
        duplicates_dict[clean_line] = []

    duplicates_dict[clean_line].append((line_num, original_line.strip()))

# 2. Find sets that have more than 1 line (the actual near-duplicates)
near_duplicate_sets = []
for key in duplicates_dict:
    if len(duplicates_dict[key]) > 1:
        near_duplicate_sets.append(duplicates_dict[key])

# 3. Print the number of sets found
print(f"Number of near-duplicate sets: {len(near_duplicate_sets)}")
print("-" * 30)

# 4. Print the first two sets found
for i in range(min(2, len(near_duplicate_sets))):
    print(f"Set {i + 1}:")
    for line_num, original in near_duplicate_sets[i]:
        print(f"{line_num}: {original}")
    print()
