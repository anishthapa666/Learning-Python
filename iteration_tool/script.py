num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

operation = input("Enter the operation to be done: ")

if operation == "+":
    print(num1 + num2)
elif operation == "*":
    print(num1*num2)
elif operation == "-":
    print(num1-num2)
elif operation == "/":
    print(num1//num2)
else:
    print("we are not abe to perform the give opweration.")