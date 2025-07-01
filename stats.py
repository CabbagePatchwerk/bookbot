#Pull text from file
def get_book_text(book):
        with open(book) as f:
                file_contents = f.read()
                return file_contents

#Count words
def word_count(book_text):
        words = book_text.split()
        return len(words)

#Count letters
def characters(book_text):
	char_count = {}
	for char in book_text:
		char = char.lower()
		char_count[char] = char_count.get(char, 0) + 1
	return char_count

def sort_letters(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list

