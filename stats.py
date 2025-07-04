def get_book_text(book: str):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def number_of_words(book: str):
    bok = get_book_text(book)
    book_array = bok.split()
    return len(book_array)

def number_of_characters(book: str):
    bok = get_book_text(book)
    bok = bok.lower()
    words_array = bok.split()
    character_count = {}
    for word in words_array:
        characters = list(word)
        for character in characters:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count



def sorted_characters(book: dict):
    def sort_on(items):
        return items["num"]

    sorted_list = []

    for character in book:
        temp_dict = {
            "Char": character,
            "num": book[character]
        }
        sorted_list.append(temp_dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list



