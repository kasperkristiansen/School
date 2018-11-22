list1 = []
list2 = []


def is_sorted(a):
    if a.isdigit():
        list1.append(a)
        list2.append(a)
        is_sorted(input("Add a number: "))
    elif a == "end":
        list1.sort()
        print(list1)
        print(list2)
        print(list_sorted(list1, list2))
    elif not a.isdigit():
        print("Invalid entry. Try again.")
        is_sorted(input("Add a number: "))


def list_sorted(a, b):
    if a == b:
        return True
    else:
        return False


is_sorted(input("Add a number: "))
