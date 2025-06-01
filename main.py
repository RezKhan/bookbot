from stats import get_num_words, get_num_chars, sort_char_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def print_report(file_path):
    book = get_book_text(file_path)
    word_count = get_num_words(book)
    sorted_chars = sort_char_dict(get_num_chars(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for chars in sorted_chars:
        if chars["char"].isalpha():
            print(f"{chars['char']}: {chars['count']}")
    print("============= END ===============")


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = args[1]
    print_report(file_path)

main()
