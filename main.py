import sys
from stats import get_num_words, count_characters, sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from the command-line arguments
book_path = sys.argv[1]

def main():
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...\n")

    # Word Count Section
    print("--------- Word Count ----------")
    num_words = get_num_words(book_path)  # Pass book_path here
    print(f"Found {num_words} total words\n")

    # Character Count Section
    print("------- Character Count -------")
    char_stats = count_characters(book_path)  # Pass book_path here
    sorted_chars = sort_characters(char_stats)

    for entry in sorted_chars:
        char = entry["char"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {entry['num']}")

    print("\n=========== END ============")

main()