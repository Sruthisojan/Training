#introduction
class Instructors:
    companyName = "QBurst"
    def __init__(self,course,duration):
        self.course = course
        self.duration = duration
    def printinfo(self):
        print("My company name is", Instructors.companyName)

elearning = Instructors("Python for beginners",7)
bls = Instructors("Django for beginners",8)

bls.printinfo()
print(bls.course)
bls.course="HTML"
print(bls.course)

#inheritance
class Persons:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
florist = Persons("Jane","Flower")
florist.printname()
class Lawyers(Persons):
    def __init__(self,fname,lname,casetype):
        self.firstname = fname
        self.lastname = lname
        self.casetype = casetype
    def printinfo(self):
        print(self.firstname,self.lastname)
happy_lawyers=Lawyers("Jack","Smiley","criminal")
happy_lawyers.printinfo()
print(happy_lawyers.casetype)

#polymorphism
def addNumbers(a,b,c=1):
    return a+b+c
print(addNumbers(8,9))
print(addNumbers(8,9,4))
#same function having different values

class UK():
    def capital(self):
        print("London is the capital of UK")
    def language(self):
        print("English is the primary language")

class Spain():
    def capital(self):
        print("Madrid is the capital of Spain")
    def language(self):
        print("Spanish is the primary language")

queen = UK()
zara = Spain()

for country in (queen,zara):
    country.capital()
    country.language()

def europe(eu):
    eu.capital()
europe(queen)
europe(zara)

#encapsulation
class Cars:
    def __init__(self,speed,color):
        self.__speed = speed # __ makes it encapsulated
        self.__color = color
    def set_speed(self,value):
        self.__speed = value
    def get_speed(self):
        return self.__speed

ford =Cars(250,"green")
nissan =Cars(300,"red")
toyota =Cars(350,"blue")

ford.set_speed(450) #when encapsulated, this will work
ford.speed=500 #when encapsulated,this wont work
print(ford.get_speed())

#abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.__side=side
    def area(self):
        return self.__side*self.__side
    def perimeter(self):
        return 4*self.__side
mysquare=Square(5)
print(mysquare.area())
print(mysquare.perimeter())

