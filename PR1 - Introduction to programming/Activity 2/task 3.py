#task 3
import time

name1 = input('What is your name?')
fav_lang1 = input('What is your favourite programming language, ' + name1 + '?')
print('Thank you ' + name1 + ', very cool!')
time.sleep(1)
name2 = input("What is your friend's name?")

if name2[-1] == 's':
    fav_lang2 = input("What is " + name2 + "' favourite programming language?")
else:
    fav_lang2 = input("What is " + name2 + "'s favourite programming language?")

print(name1 + ' loves programming in ' + fav_lang1 + ', and ' + name2 + ' likes ' + fav_lang2 + '!')

