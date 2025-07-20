import sys

from stats_test import count_words, num_of_characters, chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]

    book_text = get_text_book(bookpath)
    words_counted = count_words(book_text)
    characters = num_of_characters(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    print_report(bookpath, words_counted, chars_sorted_list)

def get_text_book(path):
    with open(path) as f:
        return f.read()
    
def print_report(bookpath, words_counted, chars_sorted_list):
    print("======== BOOKBOT ========")
    print(f"Analyzing book found at {bookpath}.")
    print("------- Word Count ------")
    print(f"Found {words_counted} total words")
    print("---- Character Count ----")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("========== END ==========")


main()