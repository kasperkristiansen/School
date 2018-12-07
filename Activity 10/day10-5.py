file_name = "cipher.txt"


def encrypt():
    with open(file_name, "a") as file:
        file.write("\n")
        for letter in what:
            if letter == " ":
                file.write("")
            else:
                file.write(chr(ord(letter) + shift))


what = input("What do you want to encrypt? : ")
choose_shift = input("How many letters would you like to shift? : ")
if choose_shift.isdigit():
    shift = int(choose_shift)
    encrypt()
else:
    print("Invalid input. Try again.")
    choose_shift = input("How many letters would you like to shift? : ")
