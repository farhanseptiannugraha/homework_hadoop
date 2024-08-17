
#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

# Reading each line from the input (stdin)
for line in sys.stdin:
    # Stripping leading and trailing spaces
    line = line.strip()
    # Splitting the line into word and count
    word, count = line.split('\t', 1)

    # Convert count from string to int
    try:
        count = int(count)
    except ValueError:
        continue

    # If the word is the same as the previous one, increment its count
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Output the word and its count
            print(f'{current_word} {current_count}')
        current_count = count
        current_word = word

# Output the last word if any
if current_word == word:
    print(f'{current_word} {current_count}')
