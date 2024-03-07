def main():
    book_path = "books/frankenstein.txt"
    text = text_content_as_string(book_path)
    print(text)
    print(f"Size of text is: {count_words(text)}")
    letters = count_letters(text)
    print(letters)


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
    return chars


main()
