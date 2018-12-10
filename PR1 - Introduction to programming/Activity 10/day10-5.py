file_name = "cipher.txt"
var = "enc"


def encrypt():
    with open(file_name, "a") as file:
        file.write("\n")
        for letter in what:
            if letter == " ":
                file.write("")
            else:
                file.write(chr(ord(letter) + shift))


while var != "end":
    what = input("What do you want to encrypt? : ")
    if what == "end":
        var = "end"
        break
    choose_shift = input("How many letters would you like to shift? : ")
    if choose_shift.isdigit():
        shift = int(choose_shift)
        encrypt()
    else:
        print("Invalid input. Try again.")
        choose_shift = input("How many letters would you like to shift? : ")
