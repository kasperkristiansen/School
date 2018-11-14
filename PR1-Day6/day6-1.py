# we need pi when calculating the area of a circle
from math import pi

# when calling rec() the program will return the equation
# filling in values for a and b returns the equation using the chosen numbers
def rec(a, b):
    return a*b

# when calling tri() the program will return the equation
# filling in values for a and b returns the equation using the chosen numbers
def tri(a, b):
    return (a*b)/2

# when calling tri2() the program will return the equation
# filling in values for a, b and c returns the equation using the chosen numbers
def tri2(a, b, c):
    s = (a+b+c)/2
    areatri2 = ((s * ((s-a) * (s-b) * (s-c)))**0.5)
    return areatri2

# when calling cir() the program will return the equation
# filling in values for a returns the equation using the chosen numbers
def cir(pi, a):
    return pi*(a*2)/2

print("Welcome!\n")

# deciding the shape. .lower() so that it doesn't matter how you write it
shape = input("What shape would you like to calculate the area of? (Rectangle, circle og triangle): ").lower()

# determining the sides
if shape == "rectangle":
    side1 = float(input("How long are the shortest sides?: "))
    side2 = float(input("How long are the longest sides?: "))
    print("The area of the rectangle is", rec(side1, side2))  # swap side1 and side2 for a and b in function

# determining the base and height
elif shape == "triangle":
    baseheightcheck = input("Do you know the base and height of the triangle? (Y/N): ").upper()
    if baseheightcheck == "Y":
        tribase = float(input("How long is the base of the triangle?: "))
        triheight = float(input("How tall is the triangle?: "))
        print("The area of the triangle is", tri(tribase, triheight))
        # swap tribase and triheight for a and b in function^

    elif baseheightcheck == "N":
        sidescheck = input("Do you know the length of all the sides? (Y/N)").upper()
        if sidescheck == "Y":
            side1 = float(input("Enter the length of the first side: "))
            side2 = float(input("Enter the length of the second side: "))
            side3 = float(input("Enter the length of the third side: "))
            print("The area of the triangle is", tri2(side1, side2, side3))
        else:
            pass

elif shape == "circle":
    radiuscheck = input("Do you know the radius? (Y/N): ").upper()
    # if the user knows the radius do this
    if radiuscheck == "Y":
        radius = float(input("What is the radius?: "))
    # if user does not know radius do this
    elif radiuscheck == "N":
        diameter = float(input("What is the diameter?: "))
        radius = diameter/2

    print("The area of the circle is", cir(pi, radius))  # swap radius for a in function

