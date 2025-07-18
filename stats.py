def count_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    num_of_characters = {}
    for char in text.lower():
        if char in num_of_characters:
            num_of_characters[char] += 1
        else:
            num_of_characters[char] = 1

    return num_of_characters

def sort_on(items):
    return items["num"]

def sort_counter(counter):
    result = []
    for count in counter:
        result.append({"char": count, "num": counter[count]})
    result.sort(reverse=True, key=sort_on)
    return result