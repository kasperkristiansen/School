player = False
total = 0

while player == False:
    num1 = int(input("Please enter a number: "))
    if num1 != 0:
        total = total + num1
        player = False
    elif num1 == 0:
        print(total)
        break