import time

my_list = []
new_list = []


def listmaker(a):
    a.append(my_list[0])
    a.append(my_list[-1])
    print(new_list)


def listmaker2(a):
    while len(my_list) < 7:
        new_element = input("Enter a number: ")
        a.append(new_element)


print(new_list)
listmaker2(my_list)
time.sleep(1)
listmaker(new_list)
