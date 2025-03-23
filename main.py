from stats import get_word_count, get_num_all_chars, sort_all_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents    
     
def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        word_count = get_word_count(text)
        char_count = get_num_all_chars(text)
        sorted_char_count = sort_all_chars(char_count)

    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_char_count:
            char = item["char"]
            count = item["count"]
            # Only print alphabetical characters
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")
    

main()