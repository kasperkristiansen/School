def capital_check(string):
    for i in string:
        if i.isupper():
            print("The string contains at least one uppercase letter.")
            break

enter_something = input("Enter something here: ")
capital_check(enter_something)
