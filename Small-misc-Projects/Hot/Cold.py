from random import random

RANDOM_NUMBER = int(random()*100)

print("DISABLE IF NOT TESTING\n",
      "Number Generated:", RANDOM_NUMBER, "\n")

print("This program gives a \"Hotter\" or \"Colder\" sign every time you insert a number, compared to the previous one."
      "\nThe goal is to have the number inputted to match the random number generated between 1 and 100\n"
      "\"Tries\" to display the number of attempts\n"
      "\"New\" restarts the program\n"
      "~~~~ inserting \"Exit\" will terminate the program ~~~~\n")


z = ""
x = eval(input("Input initial guess: "))
y2 = abs(RANDOM_NUMBER - x)
i = 0

while z != 0:
    i += 1
    x = int(input("\nInsert any number: "))
    y = abs(RANDOM_NUMBER - x)

    if x == RANDOM_NUMBER:
        print("\n~~~~~ Winner Winner Chicken Dinner ~~~~~")
    elif y < y2:
        print("\nHotter")

    elif y > y2:
        print("\nColder")
    elif y == y2:
        print("\nSame Temperature")
    else:
        print("\nError!")

    y2, y = y, 0
    z = input("\n(Press Enter to ignore) - Tries/New/Exit: ")

    if z == "Tries":
        print("\n",i)

    elif z == "New":
        print("\n~~ PROGRAM RE-INITIALIZED ~~")
        i = z = y = 0
        RANDOM_NUMBER = int(random() * 100)
        print("\nDISABLE IF NOT TESTING",
              "Number Generated:", RANDOM_NUMBER, "\n")
        x = eval(input("\nInput initial guess: "))
        y2 = abs(RANDOM_NUMBER - x)

print("end")
