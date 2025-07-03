from stats import *

def main():
    characters = number_of_characters("books/frankenstein.txt")
    print(f"{number_of_words("books/frankenstein.txt")} words found in the document.")
    #characters = sorted_characters(characters)
    print(characters)

main()