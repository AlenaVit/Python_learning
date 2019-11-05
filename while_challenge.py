import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number from 1 to {}:".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        print("Please get higher!")
    else:
        print("Please get lower!")
    guess = int(input())
    if guess == answer:
        print("Well done!")
# if guess == answer:
#    print("You've got it from first time!")
# else:
#    print("You've got it from first time!")8




