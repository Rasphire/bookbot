def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(book_path):
    book_text = get_book_text(book_path)
    num_words = len(book_text.split())
    return num_words

def count_characters(book_path):
    book_text = get_book_text(book_path).lower()
    char_counts = {}
    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list

