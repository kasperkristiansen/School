file_name = "message.txt"
encrypted_file_name = "encrypted.txt"


def read():
    with open(file_name, "r") as file:
        print(file.read())


def encrypt():
    with open(file_name, "r") as file:
        with open(encrypted_file_name, "w") as file1:
            for line in file:
                file1.write("\n")
                for letter in line:
                    file1.write(chr(ord(letter) + cipher_shift))


read()


encrypt_input = input("Do you wish to encrypt the message? : ")
if encrypt_input.lower() == "yes" or encrypt_input.lower() == "y":
    cipher_shift = input("Choose the cipher shift. : ")
    if cipher_shift.isdigit():
        cipher_shift = int(cipher_shift)
        encrypt()
    else:
        print("No.")
elif encrypt_input.lower() == "no" or encrypt_input.lower() == "n":
    pass
