__author__ = "Kasper H. Kristiansen"
import random
import time

rps = ("rock", "scissor", "paper")

comppick = random.choice(rps)

score = int(0)
compscore = int(0)

print("Welcome friend! Let's play!")

player = False

while player == False:
    comppick = random.choice(rps)
    player = input("Do you pick rock, paper or scissor? : ")
    if player == "rock" and comppick == "scissor":
        score = score++1
        compscore = compscore++0
        print("Your " + player + " smashes my " + comppick + "!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    elif player == "rock" and comppick == "paper":
        score = score++0
        compscore = compscore++1
        print("My " + comppick + " covers your " + player + "!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    elif player == "rock" and comppick == "rock":
        score = score++0
        compscore = compscore++0
        print("Looks like we both picked rock. Let's go again!\nYour score: " + str(score) + "\nComputer: " + str(compscore))

    elif player == "scissor" and comppick == "paper":
        score = score++1
        compscore = compscore++0
        print("Your " + player + " cuts my " + comppick + "!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    elif player == "scissor" and comppick == "rock":
        score = score++0
        compscore = compscore++1
        print("My " + comppick + " smashes your " + player + "!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    elif player == "scissor" and comppick == "scissor":
        score = score++0
        compscore = compscore++0
        print("Looks like we both picked scissor. Let's go again!\nYour score: " + str(score) + "\nComputer: " + str(compscore))

    elif player == "paper" and comppick == "rock":
        score = score++1
        compscore = compscore++0
        print("Your " + mypick + " covers my " + comppick + "!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    elif player == "paper" and comppick == "scissor":
        score = score++0
        compscore = compscore++1
        print("My " + comppick + " cuts your " + mypick + "!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    elif player == "paper" and comppick == "paper":
        score = score++0
        compscore = compscore++0
        print("Looks like we both picked paper. Let's go again!\nYour score: " + str(score) + "\nComputer: " + str(compscore))
    else:
        print("Looks like a typo. Try again.")
    player = False





time.sleep(0.5)