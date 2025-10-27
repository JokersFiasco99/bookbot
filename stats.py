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

def sort_on(single_dict):
    return single_dict["num"]

def dict_printer(new_dict):
    new_list = []

    for key, value in new_dict.items():
        single_dict = {}
        single_dict["char"] = key
        single_dict["num"] = value
        new_list.append(single_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
