print("_____GUESSING THE NUMBER GAME_____")

import random

rand1_int = random.randint(0, 100)

print(":: Rules for playing the Game ::\n"
      "1. You have to Guess the number between 0 to 100\n"
      "2. You have only 9 chances to Guess the right number")
print("\n"
      "\n"
      "\n")

name = str(input("Enter Your Name to begin ----> "))
namep = name.capitalize()

print("START TO GUESS YOU NUMBER")

i = 0
while (i <= 8):
    user_input = int(input("Start Guessing :: "))

    if rand1_int < user_input:
        print("The Number you have chosen is greater than the number to be guessed.\n"
              "TRY AGAIN ")
        # print("Number of GUESSES left :: ", 9-i)

    elif rand1_int > user_input:
        print("The Number you have chosen is less than the number to be guessed.\n"
              "TRY AGAIN")
        # print("Number of GUESSES left :: ", 9-i)

    elif rand1_int == user_input:
        print("HURRAY....!!!!\n",
              namep, " YOU HAVE GUESSED THE RIGHT NUMBER")
        print("Number of Guesses taken ::", i + 1)

    if rand1_int == user_input:
        print("___WINNER___\n"
              "You have guessed the number in", i, " chances")
        break
    print("Number of Guesses left ::", (8 - i))

    i = i + 1

    if i == 9:
        print("___YOU LOST___\n"
              , namep, "Try Again")
        break
