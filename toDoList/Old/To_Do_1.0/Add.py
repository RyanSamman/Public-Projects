a = open("toDo.txt", "a")

print("Enter \"Exit\" to terminate the program")

while True:
    add = input("Enter text to add to list: ")

    if add == "Exit":
        a.close()
        input()
        break
    elif add == "Read":
        print("\n" + open("toDo.txt").read())
    else:
        print(add, file=a)
