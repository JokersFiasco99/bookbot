def get_num_words(text):
    
    return len(text.split())

def get_num_characters(text):
    
    char_dict = {}

    for char in text:
        k = char.lower()
        if k in char_dict:
            char_dict[k] += 1
        else:
            char_dict[k] = 1
    return char_dict