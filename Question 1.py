# QUESTION 1
import string
from collections import Counter

# QUESTION 1
# Reading the text file and splitting into individual words
file = open("sample-file.txt", "r", encoding="utf-8")
text_data = file.read()
tokens = text_data.split()
file.close()

cleaned_tokens = []

for token in tokens:
    # Convert to lowercase
    token = token.lower()

    # Remove punctuation from the beginning and end of each word
    token = token.strip(string.punctuation)

    # Only keep words with at least two alphabetic characters
    alpha_count = 0
    for char in token:
        if char.isalpha():
            alpha_count += 1

    if alpha_count >= 2:
        cleaned_tokens.append(token)

# Count the frequencies using Counter
word_counts = Counter(cleaned_tokens)

# Get the 10 most common words and print in the "word -> count" format
top_10 = word_counts.most_common(10)

for word, count in top_10:
    print(f"{word} -> {count}")