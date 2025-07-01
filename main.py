import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import get_book_text, word_count, characters, sort_letters

book_text = get_book_text(sys.argv[1])
num_words = word_count(book_text)
chars = characters(book_text)
sorted_chars = sort_letters(chars)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for char_dict in sorted_chars:
    if char_dict["char"].isalpha():
        print(f"{char_dict['char']}: {char_dict['num']}")

print("============= END ===============")

