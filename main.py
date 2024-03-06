def main():
    book_path = "books/frankenstein.txt"
    text = text_content_as_string(book_path)
    print(text)


def text_content_as_string(path):
    with open(path, encoding="UTF-8") as file:
        return file.read()


main()
