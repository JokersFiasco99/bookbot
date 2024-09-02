def main():
    # Open the file "books/frankenstein.txt" 📖
    with open("books/frankenstein.txt") as f:
        # Read the contents of the file into a variable 📝
        file_contents = f.read()
        # Count the number of words in the file 🧮
        word_count = count_words(file_contents)
        # Count the number of each character in the file 🔢
        characters = count_characters(file_contents)

    # Print the beginning of the report 📰
    print(f"--- Begin report of books/frankenstein.txt ---")
    # Print the total word count in the document 🧾
    print(f"{word_count} words found in the document")
    print(" ")

    # Sort the characters by their count in descending order 📊
    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

    # Print each character and its count 🔍
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")

def count_words(text):
    # Split the text into words and count them 🧮
    words = text.split()
    return len(words)

def count_characters(text):
    # Create an empty dictionary to store character counts 📖
    characters = {}
    # Convert the text to lowercase to count characters case-insensitively 🔡
    text = text.lower()
    # Iterate over each character in the text 🔄
    for char in text:
        # If the character is already in the dictionary, increment its count ➕
        if char in characters:
            characters[char] += 1
        # If the character is not in the dictionary, add it with a count of 1 ➕
        else:
            characters[char] = 1
    return characters

# Call the main function to run the program 🚀
main()