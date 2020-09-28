#Simple python calculator
print()
print("Welcome to the simple calculator")
print()
print("Please select the operation: 1 = Add, 2 = Substract, 3 = multiply, 4 = divide")
Operation_Select = int(input("Select operation: "))
print()
if Operation_Select == 1:
    while True:
        print("Now enter the numbers")
        X_Select = int(input("X --> "))
        Y_Select = int(input("Y --> "))
        Operation_Answer = X_Select + Y_Select
        print()
        print("The answer is", Operation_Answer)
        break
elif Operation_Select == 2:
    while True:
        print("Now enter the numbers")
        X_Select = int(input("X --> "))
        Y_Select = int(input("Y --> "))
        Operation_Answer = X_Select - Y_Select
        print()
        print("The answer is", Operation_Answer)
        break
elif Operation_Select == 3:
    while True:
        print("Now enter the numbers")
        X_Select = int(input("X --> "))
        Y_Select = int(input("Y --> "))
        Operation_Answer = X_Select * Y_Select
        print()
        print("The answer is", Operation_Answer)
        break
elif Operation_Select == 4:
    while True:
        print("Now enter the numbers")
        X_Select = int(input("X --> "))
        Y_Select = int(input("Y --> "))
        Operation_Answer = X_Select / Y_Select
        print()
        print("The answer is", Operation_Answer)
        break
else:
    while True:
        print()
        print("Invalid answer, try again")
        break
