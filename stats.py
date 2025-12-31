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


def sort_on(d):
    return d["num"]


def sorted_dicts(char_count):
    sorted_dicts = []
    for k in char_count:
        sorted_dicts.append({"char": k, "num": char_count[k]})
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts


def report(filepath, text, num_words, char_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")

    print("============= END ===============")
