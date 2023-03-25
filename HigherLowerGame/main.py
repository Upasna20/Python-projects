# TODO 1: IMPORT THE ART AND PRINT IT.

import art, game_data, random
print(art.logo)
SCORE = 0

# TODO 2: GENERATE ANY TWO RANDOM LIST OBJECTS AND STORE IN ANOTHER LIST.
list = random.choices(game_data.data, k=2)

# TODO 3: THEN PRINT THEM SEPARATELY AS COMPARE A AND COMPARE B. ALL THIS MUST BE DONE INSIDE A WHILE TRUE LOOP.
while True:
    print("Compare A:", end=" ")
    print(list[0]['name'], "a", list[0]['description'], "from", list[0]["country"])
    print(art.vs)
    print("Against B:", end=" ")
    print(list[1]['name'], "a", list[1]['description'], "from", list[1]["country"])
# TODO 4: PROMPT THE USER FOR THE SAME AND TAKE THE INPUTS.
    ans = input("who do you think has more followers?")
# TODO 5: IF INPUT IS A THEN CHECK IF LIST[0] DATA IS GREATER THAN B I.E. LIST[1] DATA . IF INPUT IS B CHECK FOR THE OPPOSITE AND IF THE
#  INPUT IS ANYTHING ELSE THEN ASK THE USER TO ENTER AGAIN.
    if ans.lower().strip() == 'a' or ans.lower().strip() == "b":

        if not ans == "a" and list[0]['follower_count'] > list[1]["follower_count"]:
            print("Wrong answer!!!")
            break
        elif not ans == 'b' and list[1]['follower_count'] > list[0]['follower_count']:
            print("Wrong answer!!!")
            break
        else:
            print("Correct!!")
            list[0] = list[1]
            while True:
                new = random.choice(game_data.data)
                if new != list[1]:
                    break
            list[1] = new
            print("Y")
            SCORE += 1
            print(f'your score is {SCORE}')


    else:
        print("Wrong input. Enter again")
# TODO 6: IF THE ANSWER IS CORRECT IN EITHER CASE THEN TAKE THE LIST AND PERFORM SWAPPING OF LIST[1] AS LIST[0]
#  GENERATE A RANDOM OBJECT FROM THE GAMEDATA LIST AS THE SECOND OBJECT AND PUT A CONDITION THAT THEY MUSN'T BE THE SAME.
#TODO 7: ADDING SCORE: IN THE CODE FOR CORRECT ANSWER ADD 1 EACH TIME YOU HAVE A CORRECT ANSWER.
# TODO 8: TO END THE GAME YOU JUST BREAK THE WHILE LOOP.
if SCORE < 3:
    print(f"The final score is {SCORE}, you performed below average dude.")
elif 3<SCORE<5:
    print(f"The final score is {SCORE}, you performed average dude.")
elif 5<SCORE<7:
    print(f"The final score is {SCORE}, you performed above average dude.")
else:
    print(f"The final score is {SCORE}, you performed phenomenally good dude.")