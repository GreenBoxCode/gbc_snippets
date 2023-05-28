#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : MLewis
# @Site    : greenboxcode.com
# function to save a dictionary to a file
# input: dictionary, filename
# output: file with dictionary contents


def dic2file(my_dict):
    """Save a dictionary to a file"""
    try:
        with open("gbc_dict2file.txt", "w") as f:
            for key, value in my_dict.items():
                f.write(f"{key}: {value}\n")
    except Exception as e:
        print(f"Exception has occured\n{e}")
    finally:
        f.close()


# Test the function
my_dict = {"Name": "Michael", "Age": 42, "Height": 6.1}
dic2file(my_dict)

# Function to read a file into a dictionary
# input: filename
# output: dictionary


def file2dic(filename):
    """Read a file into a dictionary"""
    try:
        with open(filename, "r") as f:
            my_dict = {}
            for line in f:
                (key, val) = line.split(":")
                my_dict[key] = val
    except Exception as e:
        print(f"Exception has occured\n{e}")
    finally:
        f.close()
    return my_dict


# Test the function
my_dict = file2dic("gbc_dict2file.txt")
print(my_dict)
