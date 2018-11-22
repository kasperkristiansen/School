def letter_check(word, letter):
    count = 0
    for _ in word:
        if _ == letter:
            count += 1
    print("The letter '{}' appears {} times in the word '{}'.".format(letter, count, word))


letter_check(input("Enter a letter: "), input("Enter a word: "))
