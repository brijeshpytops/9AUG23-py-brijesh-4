"""
Encapsulation in Python is one of the fundamental principles of object-oriented programming (OOP). It refers to the concept of bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class. Encapsulation helps in hiding the internal details of an object from the outside world and restricts access to certain parts of the object. This is achieved by using access modifiers like public, private, and protected.
"""

class Person:
    def __init__(self, name, age, pin):
        self.n = name
        self.a = age
        self.__p = pin

    def display(self):
        print(self.n, self.a, self.__p)

# brijesh = Person("brijesh gondaliya", 27, 1234)
# print(brijesh.n)
# print(brijesh.a)
# print(brijesh._Person__p)
# brijesh.display()


# GETTER SETTER METHOD 

class authentication:
    def __init__(self):
        self.__pwd = "mhjavyaegd"

    # getter method
    def get_password(self):
        return self.__pwd
    
    def set_password(self, new_password):
        self.__pwd = new_password
    


brijesh = authentication()
# brijesh.pwd = "test@123"
brijesh.set_password("test@123")
print(brijesh.get_password())