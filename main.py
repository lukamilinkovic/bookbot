import sys

from stats import count_words, get_characters, sort_counter

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    num_of_characters = get_characters(book_text)
    sorted_counter = sort_counter(num_of_characters)
    report = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    for item in sorted_counter:
        if item["char"].isalpha():
            report += f"{item["char"]}: {item["num"]} \n"
    report += "============= END ==============="
    print(report)
main()