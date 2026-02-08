#QUESTION 10

def find_lines_containing(filename, keyword):
    matches = []
    search_term = keyword.lower()

    try:
        # Using 'utf-8-sig' helps if the file was saved with a BOM (common on Windows)
        with open(filename, 'r', encoding='utf-8-sig') as file:
            for line_num, line_content in enumerate(file, 1):
                # Clean the line and check case-insensitively
                if search_term in line_content.lower():
                    matches.append((line_num, line_content.strip()))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    return matches

file_name = 'sample-file.txt'
keyword_to_find = 'lorem'

results = find_lines_containing(file_name, keyword_to_find)

# Updated print statements to match your assignment logic
print(f"Total matching lines found: {len(results)}")
print("First 3 matching lines:")

if results:
    for line_num, text in results[:3]:
        print(f"Line {line_num}: {text}")
else:
    print("No matches found. Check if 'lorem' exists in the file.")