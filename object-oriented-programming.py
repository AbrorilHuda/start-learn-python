## class / object
class Variable:
    x = 10


x = Variable()
print(x.x)

class Cetak:
    def __init__(self,name,age):
        self.name = name
        self.age = age

exp1 = Cetak("anton",39)

print(exp1)

class CetakStr:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Hello {self.name} umur kamu sekarang {self.age}"

exp2 = CetakStr("jamil",45)
print(exp2)

class Testing:
    def __init__(self,name,date):
        self.name = name
        self.date = date
    def hellofunc(self):
        print("hello world")

tes = Testing("name","date")
tes.hellofunc()


## inheritence
class Person:
    def __init__(self,data,ls):
        self.data = data
        self.ls = ls

class Child(Person):
    pass
    def __str__(self):
        return f"{self.data} , {self.ls}"


ch = Child("may","ok")
print(ch)

class Child2(Person):
    def __init__(self, datachil2, lschild2, year):
        super().__init__(datachil2,lschild2)
        self.year = year
    def welcome(self):
        print(f"code {self.data} tre {self.ls} licensi {self.year}")

child2 = Child2("habba","#4",2001)
child2.welcome()

##iterators

## Polymorphism
class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("hello")


r = Car("lambo","revuelto")


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1,boat1,plane1):
    x.move()



