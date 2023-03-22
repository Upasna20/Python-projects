#TODO 1: Import random and other hangman art and word file.
import random, Hangman_art, Hangman_words
print(Hangman_art.logo)
#TODO 2: Choose a random word from the hangman words.
word = random.choice(Hangman_words.word_list)
#TODO 3: Take the input from the user while lives > 0 such that lives initialised as lives = len(Stages). Also initialise a string of dashes with as many dashes as the number of alphabets in the word
# and loop ends when there is no dash left in the sequence.
lives = len(word)
seq = []
for i in range(len(word)):
    seq.append("_")

while lives > 0 and ("_" in seq):
    guess = input("Guess a letter:")
    index = 0
    exists = False
    for i in word:
        index += 1
        if guess == i:
            seq[index-1] = guess
            exists = True
    if not exists:
        lives -= 1
        print(Hangman_art.stages[lives])
    else:
        print("".join(seq))

if "_" in seq:
    print("You lose. Better luck next time!!!")
    print(f"The correct answer is {word}")






#TODO 4: Check the random word for the inputted alphabet.
#TODO 5: if the word doesn't match then , decrement lives count by 1 and then evoke the corresponding hangman art via Stages[lives].
#TODO 6: Else display the word in the form of dashes and the correct guessed word taking the right position.
#TODO 7: While looping through the random word to check for the correct word, print a dash for the wrong letter and the alphabet itself otherwise.
#TODO 8: when the loop exists then print the correct word is given when the correct word couldn't be guessed.
#TODO 9: while iterating through the word do one thing that initialise a flag called exists and if true set true along with updating the List of dashes
# at the index position where true happens for that initialise an index variable when exist is false then start conditions listed in the point 6.
# x,t,w,vc
''' improvisation ideas:
    using a known word and associated hint customised to the crowd to be catered.'''