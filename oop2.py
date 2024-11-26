class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("Person is walking")


a = Person("Jane",34,"Male")
print(a.name)
print(a.age)
a.movement()

b = Person("Mary",21,"Female")
#print(b.name)
c = Person("John", 45, "male")
#print(c.name)