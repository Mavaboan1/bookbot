from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    characters = number_of_characters(book_path)

    characters = sorted_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(book_path)} total words")
    print("--------- Character Count -------")
    for character in characters:
        if character["Char"].isalpha():
            print(f"{character['Char']}: {character['num']}")
    print("============= END ===============")
main()