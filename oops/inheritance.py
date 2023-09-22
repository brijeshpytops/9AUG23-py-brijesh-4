"""
Inheritance is one of the core concepts in object-oriented programming (OOP), and it plays a significant role in Python. Inheritance allows you to create a new class (called the derived or child class) by inheriting attributes and methods from an existing class (called the base or parent class). The derived class can then extend or override the behavior of the base class.
"""

class animal:
    def __init__(self, name):
        self.n = name

    def speak(self, voice):
        return f"Name : {self.n} \nvoice : {voice}"

class a(animal):
    def speak(self, voice):
        self.__init__(self.n)
        return super().speak(voice)

# d = a("dog")
# print(d.speak("Bho Bho"))

# c = a("cat")
# print(c.speak("miau miau"))

# # single inharitance
# class A:
#     def a(self):
#         print("I amf from class A")

# class B(A):
#     def b(self):
#         print("I amf from class B")

# b1 = B()
# print(dir(b1))

# # multilevel inharitance
# class A:
#     def a(self):
#         print("I amf from class A")

# class B(A):
#     def b(self):
#         print("I amf from class B")

# class C(B):
#     def c(self):
#         print("I amf from class C")

# c1 = C()
# print(dir(c1))
# c1.a()
# c1.b()
# c1.c()


# # multiple inharitance
# class A:
#     def a(self):
#         print("I amf from class A")

# class B:
#     def b(self):
#         print("I amf from class B")

# class C(A, B):
#     def c(self):
#         print("I amf from class C")

# c1 = C()
# print(dir(c1))
# c1.a()
# c1.b()
# c1.c()



# herarchical inharitance
# class A:
#     def a(self):
#         print("I am from class A")

# class A1(A):
#     def a1(self):
#         print("I am from class A1")

# class B1(A):
#     def b1(self):
#         print("I am from class B2")

# class A11(A1):
#     def a11(self):
#         print("I am from class A11")

# class A111(A1):
#     def a111(self):
#         print("I am from class A111")

# class B11(B1):
#     def b11(self):
#         print("I am from class B11")

# class final(B11):
#     def b111(self):
#         print("I am from class B111")

# test = final()
# test.b111()
# test.b11()
# test.b1()
# test.a()


# class A:
#     def a(self):
#         print("I am from class A")

# class A1(A):
#     def a1(self):
#         print("I am from class A1")

# class Aleft(A1):
#     def aleft(self):
#         print("I am from class Aleft")

# class Aright(A1):
#     def aright(self):
#         print("I am from class Aright")

# class A2(A):
#     def a2(self):
#         print("I am from class A2")

# obj = C()
# print(dir(obj))