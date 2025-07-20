def count_words(book_text):
    words = book_text.split()
    return len(words)

def num_of_characters(book_text):
    characters = {}
    for char in book_text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_of_characters):
    sorted_list =[]
    for ch in num_of_characters:
        sorted_list.append({"char": ch, "num": num_of_characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list