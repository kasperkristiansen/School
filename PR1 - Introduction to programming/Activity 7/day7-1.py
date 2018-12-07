shopping_list = []


def shopping(a):
    if a == "End":
        print(shopping_list)
    else:
        shopping_list.append(a)
        shopping(input("What do you want to add?: ").capitalize())


shopping(input("What do you want to add?: ").capitalize())
