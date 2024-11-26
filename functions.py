#Built-in Library functions
y  = max(56,78,90,23,12)
print("The maximum value is",y)

x = min(67,10,45,32,67)
print("The minimum value is ",x)

z = pow(2,3)
print("The result is",z)


#User-defined Functions
def greeting():
    print("Hello there")

greeting() #Calling a function


def multiply():
    num1 = 23
    num2 = 10
    print(num1*num2)

multiply()

#Parameters and Arguments/Values
def add(a,b):
    print(a+b)

add(3,4)
add(45,69)
add(15,30)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)

employee("Eugiene Kanillar",24,"CEO","Married")
employee("Debbie Telori",22,"CTO","Single")
employee("Ezra Opande",30,"HR","Single")




