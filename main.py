### MAIN COMPONENT OF THE PROGRAM

from components.read import get_items_from_storage
from components.create import create_item

def major():

    while True:
        choice = input("""
        Hi, I'm Rex, your personal to-do list assistant
        I will help you organize your to-do list and you can create lists in advance i.e have multiple to-do lists.
        This is a virtual list, so it is only stored as long as the program is running.
        
        What action would you like to perform?
        1. Create a to-do list. (c)
        2. Read a to-do list. (r)
        3. Update a to-do list. (u)
        4. Delete a to-do list. (d)
        5. Quit. (q)

        """)

        if choice == "c":
            create_item()
        if choice == "r":
            get_items_from_storage()
        if choice == "u":
            pass
        if choice == "d":
            pass
        if choice == "q":
            break

if __name__ == '__main__':
    major()