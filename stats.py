from typing import Dict

def get_word_count(whole_book: str) -> str:
    return f"Found {len(whole_book.split())} total words"

def get_letter_count(whole_book: str) -> Dict[str, int]:
    
    count_words = {}

    for char in whole_book:
        c = char.lower()
        if c in count_words:
            count_words[c] += 1
        else:
            count_words[c] = 1

    return count_words

def sort_letter_count(letter_count: Dict[str, int]) -> Dict[str, int]:
    return dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

def beautify_letter_dict(letter_dict: Dict[str, int]) -> str:
    res = []

    for letter, amount in letter_dict.items():
        if not letter.isalpha():
            continue
        res.append(f"{letter}: {amount}")

    return "\n".join(res)