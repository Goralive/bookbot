def main():
    book_path = "books/frankenstein.txt"
    text = text_content_as_string(book_path)
    words = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    # foreach through list of list_of_dict
    print("--- End report ---")


def text_content_as_string(path):
    with open(path, encoding="UTF-8") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    list_of_dict = list(chars.items())
    return list_of_dict


main()
