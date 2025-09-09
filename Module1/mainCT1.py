# File: mainCT1.py
# Written by: Angel Hernandez
# Description: Module 1 - Critical Thinking
# Requirement(s): Linear search algorithm

import os

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def linear_search(database, sought_item):
    if database and sought_item.strip():
        for index, item in enumerate(database):
            if item == sought_item:
                return index
    return -1

def main():
    try:
        clear_screen()
        print('*** Module 1 - Critical Thinking ***\n')
        search_item = "Laptop"
        marketplace_items = ["Shoes", "Book", "Microphone", "Laptop", "Desk", "Monitor"]
        result = linear_search(marketplace_items, search_item)
        message = f"Item '{search_item}' not found." if result == -1 else f"Item '{search_item}' found at index {result}."
        print(message)
    except Exception as e:
        print(e)

if __name__ == '__main__': main()
