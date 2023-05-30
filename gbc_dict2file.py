#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : MLewis
# @Site    : greenboxcode.com
# function to save a dictionary to a file
# input: dictionary, filename
# output: file with dictionary contents
import os
import warnings


def dict2file(my_dict):
    """Append a dictionary to a file"""
    try:
        with open("gbc_dict2file.txt", "a") as f:
            for key, value in my_dict.items():
                f.write(f"{key}: {value}\n")
    except Exception as e:
        print(f"Exception has occured\n{e}")
    finally:
        f.close()


# Test the function
my_dict = {"Name": "Michael", "Age": 42, "Height": 6.1}

dict2file(my_dict)



# Function to read a file into a dictionary
# input: filename
# output: dictionary
def file2dict(filename):
    """Read a file into a nested dictionary"""
    my_dict = {}
    try:
        key = ""
        value = ""
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    key, value = line.split(":")
                    my_dict[key] = value
    except Exception as e:
        print(f"Exception has occured in function file2dict()\n{e}")
    finally:
        f.close()
    return my_dict


# Test the function
my_dict = file2dict("gbc_dict2file.txt")
print(my_dict)
