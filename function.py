"""
specific task
syntax : 
def function_name(para1, para2.. paran....):
    # block of code

function call
function_name(para1, para2.. paran....)
"""


# def sum(num1, num2):
#     total = num1 + num2
#     z = 50
#     # print(total)
#     return total, z

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

# positional para
# def sum(a,b,c):
#     print(a + b + c)

# sum(10,20, 30)

# default parameters
# def bill(pen=10):
#     print(pen)
# bill(pen=30)
# bill()

# keywords para
# def bill(tomato=50, potato=30):
#     total = tomato + potato
#     print(total)
# bill()

# variable length para
# def bill(**products):
#     total = 0
#     for k, v in products.items():
#         total += v
#         print(k, v)
#     print("Totale amount : ", total)

# bill(pen=20, milk=23, chips=20, onion=15, cabbage=20)

# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     print(total)

# sum(1,2,3,4,5,6,7,8,9,10, 100)

# def test(name="brijesh", a):
#     print("?hello")
# test(20)

# def test(a, name="brijesh"):
#     print("?hello")
# test(20)


# sum = lambda x,y,z : print(x+y+z)
# sum(10,20,30)

# a = 10

# def run():
#     global a
#     # a = 10
#     print(a)

# run()
# print(a)

# def lowerCase(func):
#     def wrapper():
#         return func(name_.lower())
#     return wrapper

# @lowerCase
# def string(name):
#     return  name
# name_  = input("Enter your name : ")
# print(string(name_))