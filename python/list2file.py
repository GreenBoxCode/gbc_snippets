# read a list into a file
# input: list, filename
# output: file with list contents
# import os
# import warnings
#
#
def list2file(my_list):
  """Append a list to a file"""
  try:
    with open("gbc_list2file.txt", "a") as f:
      for item in my_list:
        f.write(f"{item}\n")
  except Exception as e:
    print(f"Exception has occured in function list2file()\n{e}")
  finally:
    f.close()

# Create a list to test the function
my_list = ["Michael", 42, 6.1] # list of strings, integers, and floats

list2file(my_list)

# function to read a file and insert into a list
# input: filename
# output: list
def file2list(filename):
  """Read a file into a list"""
  my_list = []
  try:
    with open(filename, "r") as f:
      for line in f:
        line = line.strip()
        if line:
          my_list.append(line)
  except Exception as e:
    print(f"Exception has occured in function file2list()\n{e}")
  finally:
    f.close()
  return my_list

# Test the function
my_list_read = file2list("gbc_list2file.txt")
print(my_list_read)



