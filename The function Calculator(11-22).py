def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print("===Choose an operation you would like to perform. It could be: addition<+>,subtraction<->,multiplication<*>,division</>===")

choice = input("Enter Operation:")

try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice == "+":
        print("Result:",add(num1,num2))
    elif choice == "-":
        print("Result:",subtract(num1,num2))
    elif choice == "*":
        print("Result:",multiply(num1,num2))
    else: 
        print("Result:",divide(num1,num2))

except ValueError:
    print("Error:Please enter a valid number only.")
except ZeroDivisionError:
    print("Error:Cannot divide by zero.")