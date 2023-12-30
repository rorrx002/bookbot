def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    # Print the report
    print_report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    # Convert the dictionary to a list of tuples
    chars_list = list(chars_dict.items())

    # Sort the list based on the second element of each tuple (the count)
    chars_list.sort(key=lambda x: x[1], reverse=True)

    # Print character counts
    for char, count in chars_list:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()