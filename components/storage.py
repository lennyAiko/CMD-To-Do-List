### THE STORAGE TO HOLD ALL LISTS

store = {}

def store_item(key, value, dictionary=store):
    dictionary[key] = value
    return dictionary

def get_all_titles(dictionary=store):
    buffer = []
    
    for key, items in dictionary.items():
        buffer.append(key)
    
    return buffer

def get_item(index, dictionary=store):
    return dictionary[index]
