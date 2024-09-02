def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        characters = count_characters(file_contents)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(" ")

    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

main()