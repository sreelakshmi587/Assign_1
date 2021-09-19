print(f"Welcome to the game of Tic-Tac-Toe...Be ready to roll on...")
game_board={7:' ',8:' ',9:' ',4:' ',5:' ',6:' ',1:' ',2:' ',3:' '}
symbol_chosen={}
Winner={}
board_history=[]
i=1;j=1
storing=[]

def display_board(board):
  for i in board:
      print('|', board[i], '|', end="")
      if i % 3 == 0:
          print()

def player_input():
    symbol = ''
    while symbol != 'X' and symbol != 'O':
        symbol = input("User:Please Choose either X or O: ").upper()
    if symbol == "X":
        return ('X','O')
    else:
        return ('O','X')
User_choice,Computer_choice=player_input()
print(f'User chose {User_choice}''\n',f'Computer chose {Computer_choice}')

def full_board_check(board):
    for position in range(1, 10):
        if board[position]==' ':
            return False
    return True

computer_position= 0; user_position=0
def player_choice(board):
    user_position = int(input('Choose a position[0-9]: '))
    if user_position <= 9:
        if board[user_position] == ' ':
            board[user_position] = User_choice
        else:
            print("Place is already occupied,pls choose another position")
            player_choice(board)
    elif full_board_check(board)==True:
        return 0
    return user_position

import random
def computer_choice(board):
    computer_position = random.choice(list(range(1,10)))
    if board[computer_position] == ' ':
        board[computer_position] = Computer_choice
        print(f"computer selection:{computer_position}")
    elif full_board_check(board)==True:
        return 0
    else:
        computer_choice(board)
    return computer_position

def winning_criteria(board,symbol):
    win_data=[[1,2,3],[4,5,6],[7,8,9],[7,4,1],[8,5,2],[9,6,3],[7,5,3],[9,5,1]]
    for x in range(len(win_data)):
        if board[win_data[x][0]]==symbol and board[win_data[x][1]]==symbol or board[win_data[x][2]]==symbol:
            return True
    return False
print(display_board(game_board))
while i <=10:
    game_board={7:' ',8:' ',9:' ',4:' ',5:' ',6:' ',1:' ',2:' ',3:' '}
    print(f'Game{i}..' )
    j = 1
    while not full_board_check(game_board):
        print(f"Round{j}")
        User_turn = player_choice(game_board)
        Computer_turn = computer_choice(game_board)
        print(display_board(game_board))
        if winning_criteria(game_board, User_choice) == True:
            Winner[i] = 'User'
        elif winning_criteria(game_board, Computer_choice):
            Winner[i] = 'Computer'
        symbol_chosen[j] = [User_choice, Computer_choice]
        j = j + 1
    storing.append(Winner[i])
    board_history.append(game_board)
    i = i + 1

c = 'y'
while(c == 'y'):
    try :
      ktg= int(input("Enter the game number you want to know about:"))
      print(storing[ktg - 1])
      print(f"The gameboard corresponding to the game {ktg} is:\n ")
      print(display_board(board_history[ktg - 1]))
    except :
        print("The game doesn't exist")
    c = input("Do you wish to continue the game y/n: ")















