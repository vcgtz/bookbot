def count_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}

    for char in text:
        lower_char = char.lower()

        if not lower_char in chars:
            chars[lower_char] = 0

        chars[lower_char] += 1

    return chars

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    my_list = []

    for key, val in dictionary.items():
        my_list.append({"name": key, "num": val})

    my_list.sort(reverse=True, key=sort_on)

    return my_list
