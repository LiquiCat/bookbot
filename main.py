#!/usr/bin/python3

from stats import get_word_count

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        whole_file = file.read()

    return whole_file

def main():

    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(word_count)


if __name__ == "__main__":
    main()