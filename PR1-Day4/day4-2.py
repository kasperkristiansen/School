tempwhat = input("Are you converting from Celsius, Fahrenheit or Kelvin?: ")
temp1 = input("Please enter a temperature: ")
converted = input("Would you like to convert to Celsius, Fahrenheit or Kelvin: ")
temp2 = 20


if tempwhat == "Celsius" and temp1 != "":
    if converted == "Fahrenheit":
        print(temp1, "degrees Celsius is", 9 / 5 * float(temp1) + 32, "degrees Fahrenheit.")
    elif converted == "Kelvin":
        print(temp1, "degrees Celsius is", float(temp1) + 273.15, "degrees Kelvin.")
    elif converted == "":
        print(temp1, "degrees Celsius is", 9 / 5 * float(temp1) + 32, "degrees Fahrenheit")
        print(temp1, "degrees Celsius is", float(temp1) + 273.15, "degrees Kelvin")

elif tempwhat == "Fahrenheit" and temp1 != "":
    if converted == "Celsius":
        print(temp1, "degrees Fahrenheit is", 5/9 * (float(temp1) - 32), "degrees Celsius.")
    elif converted == "Kelvin":
        print(temp1, "degrees Fahrenheit is", (float(temp1) + 459.67) * 5/9), "degrees Kelvin."
    elif converted == "":
        print(temp1, "degrees Fahrenheit is", 5 / 9 * (float(temp1) - 32), "degrees Celsius.")
        print(temp1, "degrees Fahrenheit is", (float(temp1) + 459.67) * (5 / 9), "degrees Kelvin.")

elif tempwhat == "Kelvin" and temp1 != "":
    if converted == "Celsius":
        print(temp1, "degrees Kelvin is", (float(temp1) - 273.15), "degrees Celsius.")
    elif converted == "Fahrenheit":
        print(temp1, "degrees Kelvin is", (float(temp1) - 273.15) * 1.8 + 32, "degrees Fahrenheit.")
    elif converted == "":
        print(temp1, "degrees Kelvin is", (float(temp1) - 273.15), "degrees Celsius.")
        print(temp1, "degrees Kelvin is", (float(temp1) - 273.15) * 1.8 + 32, "degrees Fahrenheit.")

elif tempwhat == "Celsius" and temp1 == "":
    if converted == "Celsius":
        print(temp2, "degrees Fahrenheit is", 5/9 * (temp2 - 32), "degrees Celsius.")
    elif converted == "Kelvin":
        print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * 5/9), "degrees Kelvin."
    elif converted == "":
        print(temp2, "degrees Fahrenheit is", 5 / 9 * (temp2 - 32), "degrees Celsius.")
        print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * (5 / 9), "degrees Kelvin.")

elif tempwhat == "Fahrenheit" and temp1 == "":
    if converted == "Celsius":
        print(temp2, "degrees Fahrenheit is", 5/9 * (temp2 - 32), "degrees Celsius.")
    elif converted == "Kelvin":
        print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * 5/9), "degrees Kelvin."
    elif converted == "":
        print(temp2, "degrees Fahrenheit is", 5 / 9 * (temp2 - 32), "degrees Celsius.")
        print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * (5 / 9), "degrees Kelvin.")

elif tempwhat == "Kelvin" and temp1 == "":
    if converted == "Celsius":
        print(temp2, "degrees Fahrenheit is", 5/9 * (temp2 - 32), "degrees Celsius.")
    elif converted == "Kelvin":
        print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * 5/9), "degrees Kelvin."
    elif converted == "":
        print(temp2, "degrees Fahrenheit is", 5 / 9 * (temp2 - 32), "degrees Celsius.")
        print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * (5 / 9), "degrees Kelvin.")

elif tempwhat == "":
    if temp1 == "":
        if converted == "Celsius":
            print(temp2, "degrees Fahrenheit is", 5 / 9 * (temp2 - 32), "degrees Celsius.")
            print(temp2, "degrees Kelvin is", (temp2 - 273.15), "degrees Celsius.")
        elif converted == "Fahrenheit":
            print(temp2, "degrees Celsius is", 9 / 5 * temp2 + 32, "degrees Fahrenheit")
            print(temp2, "degrees Kelvin is", (temp2 - 273.15) * 1.8 + 32, "degrees Fahrenheit.")
        elif converted == "Kelvin":
            print(temp2, "degrees Celsius is", temp2 + 273.15, "degrees Kelvin")
            print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * (5 / 9), "degrees Kelvin.")
    elif temp1 != "":
        print(temp1, "degrees Celsius is", 9 / 5 * float(temp1) + 32, "degrees Fahrenheit.")
        print(temp1, "degrees Celsius is", float(temp1) + 273.15, "degrees Kelvin.")
        print(temp1, "degrees Fahrenheit is", 5 / 9 * (float(temp1) - 32), "degrees Celsius.")
        print(temp1, "degrees Fahrenheit is", (float(temp1) + 459.67) * (5 / 9), "degrees Kelvin.")
        print(temp1, "degrees Kelvin is", (float(temp1) - 273.15), "degrees Celsius.")
        print(temp1, "degrees Kelvin is", (float(temp1) - 273.15) * 1.8 + 32, "degrees Fahrenheit.")


elif temp1 == "" and tempwhat == "" and converted == "":
    print(temp2, "degrees Celsius is", 9 / 5 * temp2 + 32, "degrees Fahrenheit")
    print(temp2, "degrees Celsius is", temp2 + 273.15, "degrees Kelvin")
    print(temp2, "degrees Fahrenheit is", 5 / 9 * (temp2 - 32), "degrees Celsius.")
    print(temp2, "degrees Fahrenheit is", (temp2 + 459.67) * (5 / 9), "degrees Kelvin.")
    print(temp2, "degrees Kelvin is", (temp2 - 273.15), "degrees Celsius.")
    print(temp2, "degrees Kelvin is", (temp2 - 273.15) * 1.8 + 32, "degrees Fahrenheit.")


else:
    print("Unable to read, please try again.")

