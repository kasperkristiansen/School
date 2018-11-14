from random import randint

player = False

def wanttoquit(a):
    if a == "quit":
        quit()

print("Welcome! I will pick a random number, can you guess it?")
lowest = input("What would you like the lowest number to be?: ")
wanttoquit(lowest)
highest = input("What would you like the highest number to be?: ")
wanttoquit(highest)
attempts = input("How many attempts would you like?: ")
wanttoquit(attempts)

totalattempts = 0
compnumber = randint(int(lowest), int(highest))

while player == False:
    num1 = input("Can you guess my number?: ")
    if int(attempts) > 0:
        if num1 == "quit":
            break
        elif int(num1) > compnumber:
            attempts = int(attempts) - - 1
            totalattempts += 1
            print("\nToo high!", attempts, "attempts left!")
        elif int(num1) < compnumber:
            attempts = int(attempts) - - 1
            totalattempts += 1
            print("\nToo low!", attempts, "attempts left!")
        elif int(num1) == compnumber:
            totalattempts += 1
            print("\nYou guessed my number in", totalattempts, "attempts! Gongratulations!")
            break
    elif int(attempts) == 0:
        print("\nYou lost!")
        break