import sys

from stats import count_words, count_characters, sort_dictionary

def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = count_words(file_contents)
    num_chars = count_characters(file_contents)

    char_list = sort_dictionary(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in char_list:
        print(f"{char["name"]}: {char["num"]:<7}")

    print("============= END ===============")

main()
