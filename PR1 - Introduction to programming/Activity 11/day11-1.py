import cat
import dog
import snake
import hamster

print('Welcome home.')
dog.home(), cat.home()
choose_pet = input('\nChoose a pet: ')
if choose_pet.lower() == 'dog':
    dog.festive()
elif choose_pet.lower() == 'cat':
    cat.nap()
elif choose_pet.lower() == 'snake':
    snake.snake()
elif choose_pet.lower() == 'hamster':
    hamster.running()
else:
    print('You don\'t own that pet, dude')


name_dog = input('\nWhat is the name of your dog? : ').capitalize()
name_cat = input('What is the name of your cat? : ').capitalize()
name_hamster = input('What is the name of your hamster? : ').capitalize()
name_snake = input('What is the name of your snakes? : ').capitalize()

dog.greeting(name_dog)
cat.greeting(name_cat)
hamster.running(name_hamster)
snake.snake(name_snake)
