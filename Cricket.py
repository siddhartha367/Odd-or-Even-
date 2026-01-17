# Our classic Odd or Even game.
# Made into a Cricket game.

import random

#funtions

"""
def user_batting():
    user_score = 0
    while True:
        r=0
        try:
            user_run = int(input("Enter your run (1-6): "))
            if not (1 <= user_run <= 6):
                print("Invalid input! Enter number between 1 and 6.")
                print("Re-bat!")
                r=1
                continue   # stay in loop and ask again
        # valid input → proceed with game logic
            #break
        except ValueError:
            print("Invalid input! Numbers only.")
            print("Re-bat!")
            r=1
        if r==0:
            computer_ball = random.randint(1, 6)
            print(f"Computer chose: {computer_ball}")
        if user_run == computer_ball:
            print("That's out!")
            print(f"Your score: {user_score}")
            break
        else:
            user_score += user_run
            print(f"Your score: {user_score}")
    return user_score

def computer_batting():
    computer_score = 0
    while True:
        try:
            user_ball = int(input("Enter your bowl (1-6): "))
            if not (1 <= user_ball <= 6):
                print("Invalid input! Enter number between 1 and 6.")
                print("Re-bowl!")
                continue
            #break
        except ValueError:
            print("Invalid input! Numbers only.")
            print("Re-bowl!")
        computer_run = random.randint(1, 6)
        print(f"Computer chose: {computer_run}")
        if computer_run == user_ball:
            print("Computer is out!")
            print(f"Computer's score: {computer_score}")
            break
        else:
            computer_score += computer_run
            print(f"Computer's score: {computer_score}")
    return computer_score


def user_batting_1():
    if user_batting() > computer_batting():
        diff = user_batting() - computer_batting()
        print(f"You won by {diff} runs!")
    elif user_batting() < computer_batting():
        diff = computer_batting() - user_batting()
        print(f"Computer won by {diff} runs!")
    else:
        print(f"It's a tie! Both of you have {user_batting()} runs!")

def computer_batting_1():
    if computer_batting() > user_batting():
        diff = computer_batting() - user_batting()
        print(f"Computer won by {diff} runs!")
    elif computer_batting() < user_batting():
        diff = user_batting() - computer_batting()
        print(f"You won by {diff} runs!")
    else:
        print(f"It's a tie! Both of you have {computer_batting()} runs!")
"""

def user_batting():
    user_score = 0

    while True:
        try:
            user_run = int(input("Enter your run (1-6): "))
            if not (1 <= user_run <= 6):
                print("Invalid input! Enter number between 1 and 6.")
                print("Re-bat!")
                continue
        except ValueError:
            print("Invalid input! Numbers only.")
            print("Re-bat!")
            continue   # 🔑 THIS was missing

        computer_ball = random.randint(1, 6)
        print(f"Computer chose: {computer_ball}")

        if user_run == computer_ball:
            print("That's out!")
            print(f"Your score: {user_score}")
            break
        else:
            user_score += user_run
            print(f"Your score: {user_score}")

    return user_score

def computer_batting():
    computer_score = 0

    while True:
        try:
            user_ball = int(input("Enter your bowl (1-6): "))
            if not (1 <= user_ball <= 6):
                print("Invalid input! Enter number between 1 and 6.")
                print("Re-bowl!")
                continue
        except ValueError:
            print("Invalid input! Numbers only.")
            print("Re-bowl!")
            continue   # 🔑 prevents ball from being played

        computer_run = random.randint(1, 6)
        print(f"Computer chose: {computer_run}")

        if computer_run == user_ball:
            print("Computer is out!")
            print(f"Computer's score: {computer_score}")
            break
        else:
            computer_score += computer_run
            print(f"Computer's score: {computer_score}")

    return computer_score

def user_batting_1():
    user_score = user_batting()
    computer_score = computer_batting()

    if user_score > computer_score:
        print(f"You won by {user_score - computer_score} runs!")
    elif user_score < computer_score:
        print(f"Computer won by {computer_score - user_score} runs!")
    else:
        print(f"It's a tie! Both scored {user_score} runs!")

def computer_batting_1():
    computer_score = computer_batting()
    user_score = user_batting()

    if computer_score > user_score:
        print(f"Computer won by {computer_score - user_score} runs!")
    elif computer_score < user_score:
        print(f"You won by {user_score - computer_score} runs!")
    else:
        print(f"It's a tie! Both scored {computer_score} runs!")

#main code (running the game)

print("Welcome to the Cricket Game!")
print("")

"""
print("Let's play Odd or Even to decide who bats or bowls first.")
user_choice = input("Choose Odd or Even: ").strip().lower()
user_number = int(input("Enter a number between 1 and 6: "))
"""

print("Let's play Odd or Even to decide who bats or bowls first.")

# Odd / Even choice
while True:
    user_choice = input("Choose Odd or Even: ").strip().lower()
    if user_choice in ["odd", "even"]:
        break
    else:
        print("Invalid choice! Enter 'Odd' or 'Even'.")

# Number choice (1–6)
while True:
    try:
        user_number = int(input("Enter a number between 1 and 6: "))
        if 1 <= user_number <= 6:
            break
        else:
            print("Invalid input! Enter number between 1 and 6.")
    except ValueError:
        print("Invalid input! Numbers only.")


computer_number = random.randint(1, 6)
print(f"Computer chose: {computer_number}")

total = user_number + computer_number
if total % 2 == 0:
    result = "even"
else:
    result = "odd"

if user_choice == result:
    print("You win!" )
    u_bbf_choice = input("Choose Bat or Bowl first: ").strip().lower()   #bbf = bat or bowl choice.
    if u_bbf_choice == "bat":
        print("Good luck with your batting!")
        user_batting_1()
    else:
        print("Good luck with your bowling!")
        computer_batting_1()

else:
    print("Computer wins!")
    c_bbf_choice = random.choice(["bat", "bowl"])
    print(f"Computer chose to {c_bbf_choice} first.")
    if c_bbf_choice == "bat":
        print("Computer is batting first!")
        print("Good luck with your bowling!")
        computer_batting_1()
    else:
        print("Computer is bowling first!")
        print("Good luck with your batting!")
        user_batting_1()