#QUESTION 2
import string
from collections import Counter

#read file and get cleaned tokens
file = open("sample-file.txt", "r", encoding="utf-8")
text = file.read()
tokens = text.split()
file.close()

cleaned_tokens = []
for token in tokens:
    token = token.lower().strip(string.punctuation)
    # Check for at least 2 letters
    letters = 0
    for char in token:
        if char.isalpha():
            letters += 1
    if letters >= 2:
        cleaned_tokens.append(token)

# Construct bigrams
bigrams = []
for token in range(len(cleaned_tokens)-1):
    pair = f"{cleaned_tokens[token]} {cleaned_tokens[token+1]}"
    bigrams.append(pair)

# Count frequencies
bigram_counts = Counter(bigrams)

# Prints the 5 most frequent bigrams
top_5_bigrams = bigram_counts.most_common(5)

for bigram, count in top_5_bigrams:
    print(f"{bigram} -> {count}")
