number1 = input("Pick a number, fool! : ")
if int(number1) % 3 == 0:
    if int(number1) % 5 != 0:
        print("Fizz")
    elif int(number1) % 5 == 0:
        print("Fizz Buzz")
elif int(number1) % 3 != 0:
    if int(number1) % 5 == 0:
        print("Buzz")
    elif int(number1) % 5 != 0:
        print("Buzz Buzz Buzz")
