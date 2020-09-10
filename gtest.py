import random
from datetime import datetime

def randomNumber():
    random.seed(datetime.now())
    return random.randint(1, 80)

def getKenoNumbers():
    output = []
    for i in range(0, 20):
        output.append(randomNumber())
    return output

def getUserSelection():
    amount = input("How many numbers do you want to choose (2-10): ")
    if not amount.isdigit():
        print("Error bitch not an int")
    if int(amount) <= 1 or int(amount) >= 11:
        print("Out of bounds bitch")

    output = []
    while True:
        choice = input("Choose a number between 1 and 80: ")
        if not choice.isdigit():
            print("Bitch not a number u dum dum")
        if int(choice) <= 0 or int(choice) >= 81:
            print("Dum Dum there are only 80 numbers")
        output.append(int(choice))
        if len(output) == int(amount):
            break

    return output

def compareChoices(user, machine):
    output = []
    matched = 0
    matchedNumbers = []

    for item in user:
        if item in machine:
            matched += 1
            matchedNumbers.append(item)

    output.append(matched)
    output.append(matchedNumbers)
    return output





userChoices = getUserSelection()
kenoNumbers = getKenoNumbers()
results = compareChoices(userChoices, kenoNumbers)

print("User chose: {}".format(userChoices))
print("Machine chose: {}".format(kenoNumbers))
print("User matched: {} drawings, and matched these numbers: {}".format(results[0], results[1]))
