from random import randint

rps = ["rock", "paper", "scissor"]

yourpick = False

yourscore = int(0)
compscore = int(0)
roundsdefault = int(10)

print("Welcome player")
rounds = input("How many rounds would you like to play? :")
if rounds == "":
    rounds = roundsdefault

print("We will now play " + str(rounds) + " rounds! Let's start!")
#print("We will now play {} rounds! Let's start!".format(rounds))
#these will print the same result

while yourpick == False:
    comppick = rps[randint(0, 2)]
    yourpick = input("Rock, Paper or Scissor? : ").lower()
    if yourpick == comppick:
        print("Looks like we both picked " + yourpick)
        print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
        #print("Your score: {1}\nComputer: {0}".format(str(compscore), str(yourscore)))
        #these print the same result
        rounds = int(rounds) - 1
        print("You have " + str(rounds) + " rounds left.\n")
    elif yourpick == "rock":
        if comppick == "scissor":
            print("Your rock smashes my scissor!")
            yourscore = yourscore+1
            compscore = compscore+0
            print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
            rounds = int(rounds) - 1
            print("You have " + str(rounds) + " rounds left.\n")
        elif comppick == "paper":
            print("My paper covers your rock!")
            yourscore = yourscore+0
            compscore = compscore+1
            print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
            rounds = int(rounds) - 1
            print("You have " + str(rounds) + " rounds left.\n")
    elif yourpick == "scissor":
        if comppick == "rock":
            print("My rock smashes your scissor!")
            yourscore = yourscore+0
            compscore = compscore+1
            print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
            rounds = int(rounds) - 1
            print("You have " + str(rounds) + " rounds left.\n")
        elif comppick == "paper":
            print("Your scissor cuts my paper!")
            yourscore = yourscore+1
            compscore = compscore+0
            print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
            rounds = int(rounds) - 1
            print("You have " + str(rounds) + " rounds left.\n")
    elif yourpick == "paper":
        if comppick == "rock":
            print("Your paper covers my rock!")
            yourscore = yourscore+1
            compscore = compscore+0
            print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
            rounds = int(rounds) - 1
            print("You have " + str(rounds) + " rounds left.\n")
        elif comppick == "scissor":
            print("My scissor cuts your paper!")
            yourscore = yourscore+0
            compscore = compscore+1
            print("Your score: " + str(yourscore) + "\nComputer: " + str(compscore))
            rounds = int(rounds) - 1
            print("You have " + str(rounds) + " rounds left.\n")
    else:
        print("Looks like a typo. Try again.")
    yourpick = False
    if rounds == 0:
        print("No more rounds. Thanks for playing!\nFinal score:\nYour score: " + str(yourscore) + "\nComputer: " + str(compscore))
        if yourscore > compscore:
            print("YOU WON!")
        elif yourscore < compscore:
            print("Sorry. You lost!")
        else:
            print("Good game, it's a tie!")
        break