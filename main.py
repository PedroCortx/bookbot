from stats import get_book_text, get_num_words, get_char_count, sorted_dicts, report
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_list = sorted_dicts(char_count)
    report(filepath, text, num_words, char_count, sorted_list)


main()
