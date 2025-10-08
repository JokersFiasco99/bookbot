from stats import get_num_words, get_num_characters, dict_printer


def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    text = get_book_text("books/frankenstein.txt")
    num_characters = get_num_characters(text)

    print("----------- Word Count ----------")

    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    sorted_list = dict_printer(num_characters)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")


if __name__ == "__main__":
    main()