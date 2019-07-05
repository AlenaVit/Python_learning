# for i in range(10):
#    print("the number now is {}".format(i))

# i = 0

#while i <= 10:
#    print("the number is {}".format(i))
#    i += 1

available = ["north", "south"]
chosen = ""

while chosen not in available:
    chosen = input("Choose a direction: ")
    if chosen == "quit":
        print("Game over!")
        break
else:
    print("Aren't you glad?")