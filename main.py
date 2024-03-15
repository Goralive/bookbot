def main():
    book_path = "books/frankenstein.txt"

    text = text_content_as_string(book_path)
    words = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document \n")
    char_dict = get_char_dict(text)
    char_sorted_list = get_list_chars_from_dict(char_dict)
    print_report(char_sorted_list)
    print("--- End report ---")


def text_content_as_string(path):
    with open(path, encoding="UTF-8") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars


def sort_on(d):
    return d["num"]


def print_report(list_of_chars):
    for item in list_of_chars:
        print(f'The \'{item["char"]}\' character was found \'{item["num"]}\' times')


def get_list_chars_from_dict(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
