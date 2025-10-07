from stats import get_num_words, get_num_characters


def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def main():

    text = get_book_text("books/frankenstein.txt")
    num_characters = get_num_characters(text)
    print(f"Found {get_num_words(text)} total words")
    print(num_characters)


if __name__ == "__main__":
    main()