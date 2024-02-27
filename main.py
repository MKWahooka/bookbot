

def main():
    book_path = "books/frankenstein.txt"
    report = get_book_report(book_path)
    print(report)

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_count = dict()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_count_to_sorted_list(char_count):
    output = list(char_count.items())
    output.sort(reverse=True, key=lambda a: a[1])
    return output

def get_book_report(book_path):
    book_content = get_book_contents(book_path)
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{count_words(book_content)} words found in the document\n\n\n"
    chars = char_count_to_sorted_list(count_chars(book_content))
    chars = filter(lambda a: a[0].isalpha(), chars)
    for char in chars:
        report += f"The {char[0]} character was found {char[1]} times\n"
    report += "--- End report ---"
    return report


main()