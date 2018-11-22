from random import randint

answers = {1: 'It is certain',
           2: 'Yes definitely',
           3: 'You don’t want to know',
           4: 'Ask me again later',
           5: 'It is unlikely',
           6: 'Oh no, not again',
           7: '42',
           8: 'That would be an ecumenical matter',
           9: 'You, sir, are an idiot',
           10: 'Ask me again later, I\'m trying to sleep'}

question = " "*1000


for answer in question:
    ask = input("Ask a question: ")
    if ask == 'stop':
        break
    else:
        print(answers[randint(1, 10)])
