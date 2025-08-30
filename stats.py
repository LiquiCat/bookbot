from typing import Dict

def get_word_count(whole_book: str) -> str:
    return f"{len(whole_book.split())} words found in the document"

def get_letter_count(whole_book: str) -> Dict[str, int]:
    
    count_words = {}

    for char in whole_book:
        c = char.lower()
        if c in count_words:
            count_words[c] += 1
        else:
            count_words[c] = 1

    return count_words