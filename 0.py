# -------------------simple calculator by using the function-------------------------
def add(x,y):
    return(x +y)
def subtract(x,y):
    return(x - y)
def multiply(x,y):
    return(x * y)
def divide(x,y):
    return(x / y)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = int(input("Enter the choice from (1,2,3,4,5): "))
    if choice in (1,2,3,4,5):
        if choice == 1:
            print("Addition of two number", num1, "and", num2, "is: ", add(num1,num2))
            print("--------------------------")
        elif choice == 2:
            print("Subtraction of two number", num1, "and", num2, "is: ", subtract(num1,num2))
            print("--------------------------")
        elif choice == 3:
            print("Multiplication of two number", num1, "and", num2, "is: ", multiply(num1,num2))
            print("--------------------------")
        elif choice == 4:
            print("Division of two number", num1, "and", num2, "is: ", divide(num1,num2))
            print("--------------------------")
        elif choice == 5:
            print("Good bye")
            print("Thank you: ")
            exit()
    else:
        print("Invalid choice try again")