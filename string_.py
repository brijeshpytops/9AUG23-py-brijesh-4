"""
string : - immutable, 
# [A-Z,a-z, 0-9, special symbols[~!@#$%^&*() ]]

Syntzx : 


"""
str_name  = 'this is a string'
str_name  = "this is a string"
str_name  = """this is a string"""
str_name  = '''this is a string'''

# print(type(str_name))
# print(len(str_name))

# access element from the string
# positive indexing 
# print(str_name[1])
# negetive indexing 
# print(str_name[-1])

# slicing 
# print(str_name[5:9])

fname = "Brijesh"
lname = 'Gondaliya'
age = 27
price = 34.8367867
# print(fname + " " + lname)

# string formating
# print(f"your name is {fname + ' ' + lname}")
# print(f"your name is {fname} {lname}")
# print("your name is {} {}".format(fname, lname))
# print("your name is {0} {1}".format(fname, lname))
# print("your name is %s %s your age is %d: price is : %.2f" % (fname, lname, age, price))

# methods
# print(dir(fname))

name  = "PyTHOn PrograMMIng LangUage"
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())

# print(name.startswith("Py"))
# print(name.startswith("py"))
# print(name.endswith("py"))


# print(name.isdigit())
# print(name.isalpha())

name = " hshjt373"
# print(name.isalnum())
# print(not name.isalnum())


# l = [1,2,3,4,5,6]

# str_join = "-".join([str(num) for num in l])
# print([int(n) for n in str_join.split("-")])

str = "   sjafgnyt jyhfjsdah      "
# print(len(str))

print(str.lstrip())
print(str.rstrip())
print(str.strip())


















# name_ = ''
# for ch in range(len(name)):
#     print(name.index('P'), "--0--0--0-")
#     if name[ch] == 'P' and name.index('P') == 0:
#         name_ += 'J'
#         continue
#     else:
#         name_ += name[ch]










