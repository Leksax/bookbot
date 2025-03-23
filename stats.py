def get_word_count(text):
    words = text.split()
    return len(words)


def get_num_all_chars(text):
    all_chars = {}
    lowercasetext = text.lower()
    for x in lowercasetext:
        if x in all_chars:
           all_chars[x] += 1
        else: 
           all_chars[x] = 1 
    return all_chars

def sort_all_chars(all_chars):
    # Create a helper function to tell sort() which key to use
    def sort_on(dict):
        return dict["count"]

    # Convert the dictionary to a list of dictionaries    
    char_list = []
    for char, count in all_chars.items():
        char_list.append({"char": char, "count": count})

    # Sort the list (highest count first)        
    char_list.sort(reverse=True, key=sort_on)    


    return char_list