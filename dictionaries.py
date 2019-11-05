locations = {0: "You are in front of computer",
             1: "You are brfore brick building",
             2: "You are at the end of a hill",
             3: "You are inside a building",
             4: "You are in a valley",
             5:  "You are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "E":3, "N":5, "S":4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"w":1, "Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2, "S":1, "Q":0}}



loc = 2
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can't go this direction")