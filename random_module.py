import random

# Rock paper scissor
print("Rock paper scissors Game")


def rock(computer_selected):
    if computer_selected == "rock":
        return "tie"
    elif computer_selected == "paper":
        return "lose"
    else:
        return "win"


def paper(computer_selected):
    if computer_selected == "rock":
        return "win"
    elif computer_selected == "paper":
        return "tie"
    else:
        return "lose"


def scissor(computer_selected):
    if computer_selected == "rock":
        return "lose"
    elif computer_selected == "paper":
        return "win"
    else:
        return "tie"


choices = ["rock", "paper", "scissor"]

play = input("press g to play: ")
user_score = 0
computer_score = 0
tie = 0
rounds = 0

while play == "g" and rounds < 5:
    user_selected = input("Select skill: \n-rock\n-paper\n-scissor\nYour choice: ")
    computer_selected = random.choice(choices)

    if user_selected == "rock":
        print(f"Opponent's skill -> {computer_selected} = {rock(computer_selected)}")
        result = rock(computer_selected)
    elif user_selected == "paper":
        print(f"Opponent's skill -> {computer_selected} = {paper(computer_selected)}")
        result = paper(computer_selected)
    else:
        print(f"Opponent's skill -> {computer_selected} = {scissor(computer_selected)}")
        result = scissor(computer_selected)
    
    if result == 'win':
        user_score += 1
    elif result == 'lose':
        computer_score += 1
    else:
        tie += 1
    rounds += 1
print(f"\n\nYour Score -> {user_score}\nOpponent's score -> {computer_score}\nTie -> {tie}")
    
