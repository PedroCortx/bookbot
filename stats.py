def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
