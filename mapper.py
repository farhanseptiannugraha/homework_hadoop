
#!/usr/bin/env python
import sys

# Reading each line from input (stdin)
for line in sys.stdin:
    # Stripping any leading/trailing spaces
    line = line.strip()
    # Splitting the line into words
    words = line.split()
    # Output the word with a count of 1
    for word in words:
        print(f'{word}\t1')
