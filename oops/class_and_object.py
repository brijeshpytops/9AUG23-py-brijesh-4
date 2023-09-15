# class class_name:
    #  code of block
    #  data member
    #  member function

# object_name = class_name()
# object_name.data
# object_name.function_name()

import pandas as pd

# class person:
#     # data members
#     name = "brijesh"
#     age = 27

#     # member function
#     def speak(self):
#         print("I can speak")

# p1 = person()
# print(p1.age)
# print(p1.name)
# p1.speak()


class person:
    # constructor
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def show(self):
        print("Person information:")
        print("Fullname : ", self.n)
        print("Age :", self.a)
        
    
# brijesh = person("briejsh gondaliya", 27)
# # print(dir(brijesh))
# print(brijesh.n)
# print(brijesh.a)
# brijesh.show()

# ravi = person("ravi gondaliya", 27)
# # print(dir(brijesh))
# print(ravi.n)
# print(ravi.a)
# ravi.show()


total_members = int(input("Enter a number : "))

start = 1
users = list()
while(start <= total_members):
    user = {}
    name = input("Enter name : ")
    age = int(input("Enter age :"))
    p = person(name, age)
    user['name'] = p.n
    user['age'] = p.a
    users.append(user)
    start += 1

print(users)

# Create a DataFrame
df = pd.DataFrame(users)

# Specify the Excel file name and sheet name
excel_file = 'example.xlsx'
sheet_name = 'Sheet1'

# Save the DataFrame to Excel
df.to_excel(excel_file, sheet_name=sheet_name, index=False)

print(f"Data saved to '{excel_file}' in sheet '{sheet_name}'.")

# l = list()
# print(dir(l))