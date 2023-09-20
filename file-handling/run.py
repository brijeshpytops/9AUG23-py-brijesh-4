# file = open('example.txt', 'x')

# try :
#     name = input("Enter a file name: ")
#     file = open(name + '.txt', 'x')
# except FileExistsError:
#     print("This file is already exist")
# else:
#     print(f"File created!!! - '{name}.txt'")



# name = input("Enter a file name: ")
# file = open(name + '.txt', 'w')
# some_text = input("Enter some text: ")
# file.write(some_text)
# file.close()

file = open('test.txt', '+r')
# print(file.read())
# print(file.read(7))
# print(file.readline())
# print(file.readline())
# print(file.readline())
lines = file.readlines()
lines[4] = 'this is a updated line - 5\n'

# file.close()
# file.writelines(lines)
# file.close()
# print(file.read())

import pandas as pd
