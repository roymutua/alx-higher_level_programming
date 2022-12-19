#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end=' ')
            print()
    except IndexError: # If the index is out of range, we just print the elements that are available
        for i in range(len(my_list)):
            print(my_list[i], end=' ')
            print()
            return len(my_list)
        else: # If no exception is raised, we return x
            return x
