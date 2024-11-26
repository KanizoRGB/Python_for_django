number = 25 #This is an integer
second = 56.78 #This a float
text = "Hello there" #This is a String
isPythonInteresting = True #This is a boolean

#Data Structures - Multiple values stored in a single variable
cars = ["Toyota","Nissan","Volkswagen"] #This is a list. A list is ordered(when you display them) and changeable/mutable
fruits =("Orange","apple","banana") #This is a tuple. It is ordered and immutable/changeable
countries = {"Kenya","Algeria","Tunisia"} #This is a set. It is unordered and immutable
student={
    "firstname":"Dony",
    "age":34,
    "course":"Web development",
    "nationality":"Kenyan"
} #Dictionary. It comes in the form of key and value pair


print(cars)
print(fruits)
print(student)
print(student["firstname"])
print(countries)

print(number)
print(second)
print(text)
print(isPythonInteresting)

#Determining a datatype in python
print(type(countries))
print(type(student))
print(type(second))

#Typecasting - Process of converting from one datatype to another
print(float(number))
print(int(second))