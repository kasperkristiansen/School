language_author = {
    "Python": "Guido van Rossum",
    "Perl": "Larry Wall",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "PL/T": "Nick Fiddian",
    "Java": "James Gosling",
    "TcL": "John Ousterhout"}

for author in language_author:
    find_author = input("Enter a lanuage: ")
    if find_author in language_author:
        print(find_author, "was developed by", language_author[find_author])
    elif find_author == "quit":
        break
    else:
        print("Invalid entry. Try again.")
