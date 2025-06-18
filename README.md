# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Bookbot Project - Complete Overview
What I Built
A command-line text analysis tool that can read any book file and provide detailed statistics about it.

Core Features
Word counting: Counts total words in any text file
Character frequency analysis: Counts how many times each letter appears
Sorted results: Displays character counts in descending order (most frequent first)
Command-line interface: Accepts any book file as an argument
Error handling: Provides helpful usage instructions when used incorrectly
Technical Skills You Applied
1. File I/O Operations

def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as f:
        return f.read()

2. Text Processing Functions

count_words(): Splits text and counts words
count_characters(): Analyzes character frequency
sort_characters_by_count(): Sorts results by frequency

3. Command-Line Argument Handling

import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

4. Data Structures

Lists for storing word arrays
Dictionaries for character counting
List of dictionaries for sorted results

5. String Formatting

F-strings for dynamic output
Multi-line strings with \n
Conditional filtering (alphabetic characters only)

Program Flow Architecture
Validation: Check if user provided correct arguments
Input: Read book file from command line argument
Processing: Analyze text for words and characters
Output: Display formatted results with headers and sections

Books Analyze
books/frankenstein.txt
books/mobydick.txt
books/prideandprejudice.txt

Example Output
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 44538
t: 29493
a: 26743
[... more character counts ...]
============= END ===============

Programming Concepts Mastered
Modular design: Separate functions for different tasks
Error handling: Graceful failure with helpful messages
Command-line tools: Building programs that accept arguments
Text processing: Real-world data analysis
Code organization: Clean, readable, well-commented code

Plus
Scalable: Works with any size text file
Reusable: Can analyze any book from Project Gutenberg
Professional: Proper error handling and user feedback
Practical: Solves a real problem (text analysis)