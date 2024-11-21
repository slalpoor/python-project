import random
import string

def g_password(lenght):
    characters = string.printable # define characters like uppercase, lowercase, digits and characters
    password = ''.join(random.choices(characters, k = lenght))
    return password
# the main function
def main():
    print("Simple Password Generator")
    try:
        lenght= int(input("Enter the desired password length: "))
        if lenght < 8 :
            print("Password lenght should be at least 8.")
        else:
            password = g_password(lenght)
            print(f"Generated Password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")
# run the program
if __name__=="__main__":
    main()