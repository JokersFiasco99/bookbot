def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    
    return len(text.split())
    

def main():

    text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(text)} total words")

    

if __name__ == "__main__":
    main()