### update status of list

## print all list

## get index of status to list to update

## get status update

## make changes

from components.storage import get_all_titles, get_item, update

def show_list():
    buffer, status, key = get_all_titles()

    print("""
    index | title | status
    ----------------------
    """)

    count = 1

    for i in buffer:
        print(f'\t{count} | {i} | {status[count-1]}')
        count += 1

    return buffer, key

def get_index():
    num = int(input("Enter index of list you want to update the status: "))
    return num

def fetch_status(buffer, index):
    query = buffer[index-1]
    return query

def update_status():
    buffer, key = show_list()

    index = get_index()

    query = fetch_status(buffer, index)

    buffer = get_item(query)

    status = int(input("Enter status of list, 0: pending and 1: completed > "))

    if status == 1:
        buffer[1] = "completed"
    
    to_store = {key: buffer}
    
    update(value=to_store)

    return



