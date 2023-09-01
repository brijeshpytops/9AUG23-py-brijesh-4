"""
if
syntax: 
if (condition):
    # block statements

Example: 
score = 25

if(score >= 30):
    print("pass")

if...else
syntax: 
if(condition):
    # block of code
else:
    # block of code

Example :
score = 25

if(score >= 30):
    print("pass")
else:
    print("Failed")


if...elif ladder
syntax: 
if(condition-1):
    # block of code
elif(condition-2):
    # block of code
elif(condition-3):
    # block of code
    .
    .
    .
else:
    # block of code

score = -2
if(score >= 0 and score <= 100):
    if(score >= 80):
        print("First class")
    elif(score >= 60):
        print("Second class")
    elif(score >= 40):
        print("Third class")
    else:
        print("Sorry, you are Failed")
else:
    print("Please enter your score between 0 to 100")

nested if, if...else ....

age = input("Enter your age : ")
age = int(age)
if(age>=18):
    weight = input("Enter your weight : ")
    weight = float(weight)
    if(weight >= 50):
        print("You can donate")
    else:
        print(f"You can not donate your weight is {weight}")
else:
    print(f"You can not donate your age is {age}")

"""

# age = input("Enter your age : ")
# age = int(age)
# if(age>=18):
#     weight = input("Enter your weight : ")
#     weight = float(weight)
#     if(weight >= 50):
#         print("You can donate")
#     else:
#         print(f"You can not donate your weight is {weight}")
# else:
#     print(f"You can not donate your age is {age}")


