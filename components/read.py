### READ A TO-DO

from components.storage import get_all_titles, get_item
from components.update import show_list

def disintegrate(items):
    print(items)
    for i in items[0]:
        print(f'~ {i}')
    print(items[2])

def get_items_from_storage():
    
    buffer = show_list()
    
    choice = int(input("Enter index of title: "))

    query = buffer[choice-1]

    buffer = get_item(query)

    disintegrate(buffer)
    
    return
