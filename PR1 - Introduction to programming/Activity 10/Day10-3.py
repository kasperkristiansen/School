poem = "Said Hamlet to Ophelia,\n" \
       "I'll draw a sketch of thee,\n" \
       "What kind of pencil shall I use?\n" \
       "2B or not 2B?"

wrong_author = 'T S Elliot'
right_author = 'Spike Milligan'
file_name = 'poem.txt'

new_poem = "Three horses on a mountain,\n" \
           "The sun is shining,\n" \
           "One eagle soaring."

new_poem_author = "Kasper H. Kristiansen"


def create_file():
    with open(file_name, "w") as file:
        file.write(poem + "\n\t- " + wrong_author)
    print("File created.\nText written:\n" + poem + "\n\t-" + wrong_author)


# create_file()

def read_file():
    print("This is the content of the file:")
    with open(file_name, "r") as file:
        print(file.read())


# read_file()

def add_to_file():
    print("The following is now added to the file:")
    with open(file_name, "a") as file:
        file.write("\n" + new_poem + "\n- " + new_poem_author)
    print(new_poem + "\n- " + new_poem_author)


# add_to_file()

def fix_author():
    print("The following has been overwritten: ")
    with open(file_name, "r+") as file:
        file.seek(102)
        file.writelines(right_author)
    print("has been changed to " + right_author)


# fix_author()
