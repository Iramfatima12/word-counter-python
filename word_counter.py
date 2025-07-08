from collections import Counter

# Read the text file
with open('text.txt', 'r') as file:
    text = file.read()

# Clean and split the text
words = text.lower().split()

# Count words
word_count = Counter(words)

# Save to CSV
with open('output.csv', 'w') as output:
    output.write("Word,Count\n")
    for word, count in word_count.items():
        output.write(f"{word},{count}\n")

print("✅ Word count complete. Output saved in output.csv.")
