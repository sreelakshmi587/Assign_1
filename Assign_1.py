import random
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
computer=0;player=0;winner=[]
a={}
for i in range(1,10):
    player_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    a[f"\n Round{i}"] =  f"\nPlayer choice = {player_action},\ncomputer choice = {computer_action}.\n"
    if player_action == computer_action:
        winner.append("None")

    elif player_action == "rock":
        if computer_action == "scissors":
            player += 1
            winner.append(f"Player won round{i}")
        else:
            computer += 1
            winner.append(f"Computer won round{i}")
    elif player_action == "paper":
        if computer_action == "rock":
            player += 1
            winner.append(f"Player won round{i}")
        else:
            computer += 1
            winner.append(f"Computer won round{i}")
    elif player_action == "scissors":
        if computer_action == "paper":
            player += 1
            winner.append(f"Player won round{i}")
        else:
            computer += 1
            winner.append(f"Computer won round{i}")

print("Choice history:",a.items())
print(f'Consolidated Score of player = {player} and Consolidated Score of computer = {computer}  ')
s = int(input('Enter the round for which you need the information: '))

print(winner[s])


