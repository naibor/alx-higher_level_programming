#!/usr/bin/python3
"""
Module: 7-add_item
adds all arguments to a python list and saves them to a file
"""
import sys


# import functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# file to save to
filename = 'add_item.json'
# check filename and load list or create empty list
try:
    new_list = load_from_json_file(filename)
except new_list.DoesNotExist:
    new_list = []
# append the arguments to the list
for item in range(1, len(sys.argv)):
    new_list.append(sys.argv[item])
# save the list to json file
try:
    save_to_json_file(new_list, filename)
except TypeError:
    pass
