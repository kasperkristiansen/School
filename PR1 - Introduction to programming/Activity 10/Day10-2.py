user_input = input("Enter a sentence: ")
word_list = user_input.split(' ')
new_sentence = ""


def reverse(a):
    global new_sentence
    for word in reversed(a):
        new_sentence += word
        new_sentence += " "
    print(new_sentence)


reverse(word_list)
