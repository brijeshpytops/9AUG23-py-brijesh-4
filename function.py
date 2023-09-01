"""
specific task
syntax : 
def function_name(para1, para2.. paran....):
    # block of code

function call
function_name(para1, para2.. paran....)
"""


def sum(num1, num2):
    total = num1 + num2
    z = 50
    # print(total)
    return total, z

# print(sum(10,20)) # None
# print(type(sum(10,20)[0]))
# print(sum(10,20)[0])

# def outer():
#     def inner1():
#         return "inner1"
    
#     def inner2():
#         return "inner2"
    
#     return inner1, inner2

# print(outer()[0]())

# def case_insensitive(func):
#     def wrapper():
#         return func.lower()

# @case_insensitive
# def test():
#     name = input("Enter a name: ")
#     return name

# print(test(case_insensitive))