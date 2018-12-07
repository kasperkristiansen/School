# def unique_elements(a):
#     unique_list1 = []
#     for item in a:
#         if item not in unique_list1:
#             unique_list1.append(item)
#     for item in unique_list1:
#         print(item)
#
#
# list1 = [1, 3, 4, 4, 5, 3, 5, 6, 8, 1, 9, 2, 2]
# print("The unique elements in the list are: ")
# unique_elements(list1)

list1 = [1, 3, 4, 5, 1, 3, 4, 5, 2]


def unique_elements(a):
    set1 = set(list1)
    list_unique = list(set1)
    for item in list_unique:
        print(item)


print("The unique elements in the list are: ")
unique_elements(list1)
