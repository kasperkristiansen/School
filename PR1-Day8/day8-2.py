def find(word, letter, offset):
    """find function.
    This function searches a word for a letter
    and then returns the index that the letter
    first appears in the word.
    """
    startfrom = offset - 1
    index = - 1
    while startfrom < len(word):
        if word[startfrom] == letter:
            return index
        index += 1
        startfrom += 1
    return -1


enter_word = input("Enter a word: ").lower()
enter_letter = input("Enter a letter: ").lower()
enter_start = int(input("Enter the starting index: "))
print(find(enter_word, enter_letter, enter_start))

