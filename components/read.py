### READ A TO-DO

from components.storage import get_all_titles, get_item


def disintegrate(items):
    for i in items[0]:
        print(f'~ {i}')
    print(items[1])


def get_items_from_storage():
    
    buffer = get_all_titles()

    print("""
    index | title
    -------------
    """)

    count = 1

    for i in buffer:
        print(f'\t{count} | {i}')
        count += 1
    
    choice = int(input("Enter index of title: "))

    query = buffer[choice-1]

    buffer = get_item(query)

    disintegrate(buffer)
    
    return
