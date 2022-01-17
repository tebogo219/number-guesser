import random

for i in range(10):
    r= int(random.randrange(11))
    answer = int(input("please guess a number "))
    if answer == r:
        print(f"coorrect guess, the number you chose is {answer} and the random number is {r}" )
        quit()
    else:
        print(f"incorrect number, the number you were looking for is {r}")






