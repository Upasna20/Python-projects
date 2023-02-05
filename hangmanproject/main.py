from hangman_art import logo, stages
from hangman_words import word_list
import random
from test import sep

str = ''
print(logo)
LIVES = 7
# count = 0
# finding the random word
word = random.choice(word_list)
print(word)
l = len(word)
# displaying the blank lines
for i in range(l):
    str += "_"
'''use things like _*l'''
# print("_"*l)
# print(str)
Str = sep(str)
while LIVES > 0:
    count = 0
    # print(Str)
    # Word = sep(word)
    # print(Word)
    guess = input('Make a guess: ').lower()
    if guess not in word:
        print('That\'s wrong, you lose one life.')
        LIVES -= 1
        print(f'{stages[LIVES]}')
    else:
        for _ in word:
            if _ == guess:
                Str[count] = guess
                # print(Str)
                print(f'You\'ve got it right!! {"".join(Str)}')
            count += 1

    if "_" not in Str:
        # print(Str)
        print('You guessed the whole word.Congratulations!!!')
        LIVES = 0

'''here angela didn't use anything as a function that i made she simply started out with a list for blank spaces and
that's all. Otherwise you are totally fine with the random word being a string, because you can iterate as well as look 
for a particular via indexing.'''