"""
# This is a small game which is based on very basic python commands known as:
#                               "Number Guessing Game"

"""
import random
PREV_SCORE = []
def showprev_score():

    """ Append the attempts """

if len(PREV_SCORE) <= 0:
    print("No Scores Found ! Let's Go You Should set a Target ! ")
else:
    print("The Previous Record is {} attempts".format(min(PREV_SCORE)))
def play_game():
    """ This is the function for playing game """
    disp_random = int(random.randint(1, 10))

    print("Hey! Player Welcome to the Number Guessing Game ")
    p_name = input("Enter The Player Name :")

    game_choice = input("Hello!,{},If You want to start the game "
                        "Kindly enter your choice (yes/no) : ".format(p_name))
    p_attempts = 0

    showprev_score()
    while game_choice.lower() == "yes":
        try:
            guess_num = input("Kindly Pick a Number between 1 and 10 : ")
            if int(guess_num) < disp_random:

                print("Guess Higher")
                p_attempts += 1

            elif int(guess_num) > disp_random:

                print("Guess Lower")
                p_attempts += 1

            elif int(guess_num) == disp_random:

                print("Great! You guessed it correct.")
                p_attempts += 1

                PREV_SCORE.append(p_attempts)

                print("You took {} attempts".format(p_attempts))

                break


            elif int(guess_num) > 10 and int(guess_num) < 0:

                print("Kindly Choose Number between 0 and 10 !")
            else:
                break

            g_attempt = str(p_attempts)
            f_operation = open("myfile.txt", "w")
            f_operation.write(p_name)
            f_operation.write(" ")
            f_operation.write(g_attempt)
        except ValueError as err:
            print("Nah! It's Invalid You gotta try again ")

            print("({})".format(err))

    while game_choice.lower() == 'no':
        print("Okay ! See you again ! Bye !")
        break

play_game()
