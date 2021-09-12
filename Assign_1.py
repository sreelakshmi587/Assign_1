import random
print("Ready for a Game?...")
what_beats_what=[(1,3),(3,2),(2,1)]
computer=0;player=0;winner=[]
history={}

for i in range(1,11):
    player_action = int(input("Enter a choice (rock[1], paper[2], scissors[3]): "))
    while player_action > 3 or player_action < 1:
        player_action= print("Enter a valid input... ")
        break
    if(player_action == 1):
        player_choice = "rock"
    elif (player_action == 2):
        player_choice = 'paper'
    else:
        player_choice = "scissors"
        
    possible_actions = [1 , 2 , 3]
    computer_action = random.choice(possible_actions)
    if (computer_action == 1):
        computer_choice = "rock"
    elif (computer_action == 2):
        computer_choice = 'paper'
    else:
        computer_action = "scissors"
    print(f'computer choice is {computer_choice}')
    
    history[i] =  [player_choice,computer_choice]
    if(player_action == computer_action):
        winner.append("None")
    elif((player_action,computer_action) in what_beats_what):
        player += 1
        winner.append(f"Player won round {i}")
    else:
        computer += 1
        winner.append(f"Computer won round {i}")

print("Choice history: ",history.items())
print(f'Consolidated Score of player = {player} and Consolidated Score of computer = {computer}  ')

if(player == computer):
    print("Oops,It's a Tie")
elif(player > computer):
    print('Player Wins the game')
else:
    print('Computer Wins the game')
choice = 'y'
while(choice=='y'):
    try: 
        Round_enquiry = int(input('Enter the round for which you need the information: '))
        print("Player Choice: ", history[Round_enquiry][0])
        print("Computer Choice: ", history[Round_enquiry][1])
        print(winner[Round_enquiry-1])
    except:
        print('Invalid Round number')
    choice = input('Do you wish to continue(y/n)?')
     



