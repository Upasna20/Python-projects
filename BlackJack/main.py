# TODO 1: import the random module and then generate two pairs of random numbers, one for the user and the other for
#  the computer.
# TODO 2: PRINT THE NUMBERS AND DISPLAY THE USER THE CURRENT STATUS.
# TODO 3: INITIALISING A BLACKJACK GLOBAL VARIABLE TO 21 AND BLACKJACK_COND = FALSE
# TODO 4: ENTER A WHILE LOOP WITH A FLAG WITH BOOLEAN VALUE OF TRUE. INSIDE THE LOOP, WE HAVE A PROMPT ASKING WHETHER IT IS A HIT OR A STAND?
# TODO 5: IF IT IS A HIT THEN CONTINUE THE LOOP IF IT IS STAND THEN BREAK. WHEN IT IS A HIT ASK FOR A NUMBER, THEN ADD THE NUMBER.
# TODO 6: IF NUMBER COUNT IS LESS THAN THE BLACKJACK CONDITION THEN LOOP CONTINUES (ALSO CONSIDER THE BLACKJACK SITUATION) BUT IF IT IS NOT THEN PRINT BUSTED AND SET FLAG TO FALSE.
# TODO 7: WHEN WE'RE OUT OF THE LOOP,AND THE BLACKJACK CONDITION IS FALSE THEN IT IS THE COMPUTER'S CHANCE TO PERFORM SO IT GENERATES RANDOM NUMBERS, ADD TO TOTAL, CHECKS THE TOTAL UNDER ITS CONDITIONS AND THEN DISPLAYS IF THINGS ARE POSITIVE.
# TODO 8: THE CONDITION TO CHECK FOR ARE GREATER THAN USER BUT LESS THAN 21 ,( PRINT WINNER), IF 21 PRINT(WINNER) IF GREATER THAN 21 GET OUT OF THE LOOP AS YOU LOSE.
#    THE LOOP CONTINUES ONLY WHEN THE TOTAL IS LESS THAN 21 AND THE USER COUNT

import random
import time

USER_COUNT = 0
DEALER_COUNT = 0
BLACKJACK = 21
DEAL_TURN = True
CARDS = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11]


def rand_num():
    nums = random.choices(CARDS, k=2)
    while nums[0] == nums[1]:
        nums = random.choices(CARDS, k=2)
    return nums


def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def score(cards):
    print(f"Score = {sum(cards)} ")


def stats():
    print(f"Dealer: {sum(DEALER_COUNT)} and You : {sum(USER_COUNT)}")


def BlackJack():
    value = False
    if sum(USER_COUNT) == 21:
        print("BlackJack for the user!!!")
        value = True

    if sum(DEALER_COUNT) == 21:
        print("BlackJack for the Dealer!!")
        value = True
    return value


USER_COUNT = rand_num()
DEALER_COUNT = rand_num()

print("User:")
print(f"{USER_COUNT[0]} + {USER_COUNT[1]} = {USER_COUNT[0] + USER_COUNT[1]}")
print("Dealer:")
print(f"{DEALER_COUNT[0]} + {DEALER_COUNT[1]} = {DEALER_COUNT[0] + DEALER_COUNT[1]}")
if not BlackJack():
    while True:
        choice = input("Hit or Stand??")
        if choice.lower().strip() == "stand":
            break
        elif choice.lower().strip() != "hit":
            print("Oops!! Wrong input enter again.")
            continue
        else:
            num = random.choice(CARDS)
            print(f"Your number is {num}")
            USER_COUNT.append(num)
            if sum(USER_COUNT) == BLACKJACK:
                score(USER_COUNT)
                print("BlackJack!! You win.")
                DEAL_TURN = False
                break
            elif sum(USER_COUNT) > BLACKJACK:
                score(USER_COUNT)
                print("Busted )-: , better luck next time.")
                DEAL_TURN = False
                break
            else:
                score(USER_COUNT)

    while DEAL_TURN:
        time.sleep(1)
        if sum(USER_COUNT) < sum(DEALER_COUNT) < BLACKJACK:
            stats()
            print("Dealer Wins!!")
            break
        elif sum(DEALER_COUNT) == BLACKJACK:
            stats()
            print("Wow it's a BlackJack condition for the Dealer!! Dealer wins (-: ")
            break
        elif sum(DEALER_COUNT) > BLACKJACK:
            stats()
            print("Oops, Busted !!!")
            print("Dealer loses, you win!!")
            break
        else:
            num = random.choice(CARDS)
            DEALER_COUNT.append(num)
            print(f"Dealer's number is {num}")
            score(DEALER_COUNT)
