from stats import get_book_text, get_num_words, get_char_count


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    c_count = get_char_count(text)
    print(f"Found {num_words} total words")
    print(c_count)


main()
