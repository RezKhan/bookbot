def get_num_words(document):
    words = document.split()
    return len(words)

def get_num_chars(document):
    chars = {}
    for char in document.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(dict):
    return dict["count"]

def sort_char_dict(unsorted_chars):
    char_dict_array = []
    for key in unsorted_chars:
        char_dict_array.append({"char": key, "count": unsorted_chars[key]})

    char_dict_array.sort(reverse=True, key=sort_on)
    return char_dict_array

