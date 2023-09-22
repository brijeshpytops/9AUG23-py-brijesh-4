from abc import ABC, abstractmethod


class animal(ABC):
    def __init__(self, name):
        self.n = name

    @abstractmethod
    def speak(self):
        pass


class Dog(animal):
    def speak(self, voice):
        self.__init__(self.n)
        print(voice)
        return super().speak()
    
class Cat(animal):
    def speak(self, voice):
        self.__init__(self.n)
        print(voice)
        return super().speak()
    
dobj = Dog("dog")
print(dir(dobj))
print(dobj.n)
dobj.speak("Bho Bho")


cobj = Cat("cat")
print(dir(cobj))
print(cobj.n)
cobj.speak("miu miu")