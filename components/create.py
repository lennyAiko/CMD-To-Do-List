### CREATE ITEMS AND STORE

from components.storage import store_item
from components.time import get_time_date

date, time = get_time_date()

def collect_items():
    buffer = []

    while True:
        message = input("~ ")

        if message.lower() == 'q':
            return buffer

        buffer.append(message + '\n')


def create_item():

    list_title = input("Enter title of the list: ")

    list_items = collect_items()

    to_do = list_items, f'created at: {time}, on: {date}'

    store_item(key=list_title, value=to_do)

    print("List stored successfully.")

    return
