def fizzbuzz(a):

    if a[0].isalpha():
        a = str(a)
        return a
    elif a[0] in "1234567890":
        a = int(a)
        if a % 3 == 0:
            if a % 5 != 0:
                return "Fizz "
            elif a % 5 == 0:
                return "Fizz Buzz "
        elif a % 3 != 0:
            if a % 5 == 0:
                return "Buzz "
            elif a % 5 != 0:
                return "zzuB "

user = False

while user == False:
    number1 = input("Pick a number! : ")
    number2 = input("Pick another number! : ")
    print(str((fizzbuzz(number1)))+str((fizzbuzz(number2))))
    user = False
