def language(lang):
    if lang == "python":
        return True
    elif lang != "python":
        return False

fav_lang = input("What is your favoutrite programming language?: ")
print("Your favourite language is Python:", language(str.lower(fav_lang)))

#fav_lang = input("What is your fav lang?: ").lower()
#if fav_lang == "python":
#    print("Your fav lang is Python = True")
#else:
#    print("Your fav lang is Python = False")
