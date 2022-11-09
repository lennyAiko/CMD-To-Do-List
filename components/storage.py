### THE STORAGE TO HOLD ALL LISTS

store = {}

def store_item(key, value, dictionary=store):
    dictionary[key] = value
    return dictionary

def get_all_titles(dictionary=store):
    buffer = []
    status = []
    
    for key, items in dictionary.items():
        buffer.append(key)
        status.append(items[1])
    
    return buffer, status, key

def get_item(index, dictionary=store):
    value = list(dictionary[index])
    return value

def update(value, dictionary=store):
    dictionary.update(value)
    return