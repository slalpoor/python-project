user_input = 'random'
data = list()
def showMenu():
    print("Menu: ")
    print("1. Add as item: ")
    print("2. Marke as done: ")
    print("3. View items: ")
    print("4. Exit: ")


while user_input != '4':
    showMenu()
    user_input = input("enter your choice: ")

    if user_input == '1':
        item = input("what is to be added? ")
        data.append(item)
        print("Added item: ", item)
    elif user_input == '2':
        item = input("what is be deleted? ")
        if item in data:
            data.remove(item)
            print("removed item:", item)
        else:
            print("item does not exist in the to_do list")
    elif user_input == '3':
        if len(data) == 0:
            print("there are no items in the to_do list.")
        else:
            print("list of to_do items are: ")
            for item in data:
                print(item)
    elif user_input == '4':
        print("Good bye")
