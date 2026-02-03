# QUESTION 1
import string
from collections import Counter

# Read the file and split tokens
with open("studentcsv", "r", encoding = "utf-8") as file:
    tokens = file.read().split()

cleaned_tokens = []

for token in tokens:
    token = token.lower()
    token = token.strip(string.punctuation)
    if sum(char.isalpha() for char in token) >= 2:
        cleaned_tokens.append(token)
word_counts = Counter(cleaned_tokens)


for word, count in word_counts.most_common(10):
    print(f"{word} -> {count}")
