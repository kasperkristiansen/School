def palindrome(a):
    if a[::-1] == a:
        return True
    else:
        return False


user_input = input("Enter a string: ")
print(palindrome(user_input))
