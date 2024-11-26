try:
    print(number)
except NameError:
    print("You must define your variable")



num1 = 39
num2 = 0


try:
    print(num1/num2)
except:
    print("ZeroDivisionError has occurred")
finally:
    print("Success")


