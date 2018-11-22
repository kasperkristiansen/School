# def in_both(string1, string2):
#    index = 0
#    for _ in string1:
#        if string2[index, (len(string1)-1)] == string1:
#            print("'", string1, "'", "can be found within", "'", string2, "'")
#        index += 1
#    for _ in string2:
#        if string1[index, (len(string2)-1)] == string2:
#            print("'", string2, "'", "can be found within", "'", string1, "'")
#        index += 1


def in_both(string1, string2):
    if string1 in string2:
        print("'", string1, "' can be found within '", string2, "'.")
    elif string2 in string1:
        print("'", string2, "' can be found within '", string1, "'.")
    else:
        print("None of the sentences can be found within the other")


in_both(input("Enter first sentence: "), input("Enter second sentence: "))
