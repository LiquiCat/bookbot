#!/usr/bin/python3

import sys

from stats import get_word_count, \
                    get_letter_count, \
                    sort_letter_count, \
                    beautify_letter_dict

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        whole_file = file.read()

    return whole_file

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    sorted_letters = sort_letter_count(get_letter_count(book_text))
    letters_column = beautify_letter_dict(sorted_letters)

    final_message = f"""============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------
{word_count}
--------- Character Count -------
{letters_column}
============= END ===============
"""
    print(final_message)


if __name__ == "__main__":
    main()