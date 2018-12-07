set1 = {0}
set2 = {0}


def enternumbers(a, b):
    while len(a) < 10:
        print(b)
        enter_number = input("Enter a number: ")
        a.add(int(enter_number))


enternumbers(set1, "Set 1")
enternumbers(set2, "Set 2")

for element in set1:
    if element in set2:
        print(element, "is in both sets.")
    elif element not in set2:
        print(element, "is exclusive to set 1.")

for element in set2:
    if element not in set1:
        print(element, "is exclusive to set 2.")