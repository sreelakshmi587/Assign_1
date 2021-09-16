
def display_board(board):
    print('\n'*10)

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print("\t     |     |")
    print("\n")


def player_input():
    symbol = ''
    while symbol!='X' and symbol!='O':
        symbol= input("User:Please Choose either X or O: ").upper()
    if symbol == "X":
        return ('X','O')
    else:
        return ('O',X)



User,Computer = player_input()

def place_symbol(board,symbol,position):
    board[position] = symbol

def win_check(board,symbol):

    return ((board[1]==symbol and board[2]==symbol and board[3]==symbol) or
            (board[4] == symbol and  board[5] ==symbol and  board[6] == symbol) or
            (board[7] == symbol and  board[8] == symbol and board[9] == symbol) or
            (board[7] == symbol and  board[4] == symbol and  board[1] == symbol) or
            (board[8]== symbol and board[5]==symbol and board[1]==symbol) or
            (board[9] == symbol and board[6] == symbol and  board[3] == symbol) or
            (board[7]== symbol and board[5]==symbol and board[3]==symbol) or
            (board[9] == symbol and  board[5] ==symbol and  board[1] == symbol))
import random
def who_first():
    flip= random.randint(0,1)
    if flip ==0:
        return 'User'
    else:
        return 'Computer'

def game_space_check(board,position):
    return board[position]==' '
def full_board_check(board):
    for i in range(1,10):
        if game_space_check(board,i):
            return False
    return True
def player_choice(board):
    position = 0
    while position not in range(1,10) or not game_space_check(board,position):
        position= int(input('Choose a position[0-9]: '))
    return position
def replay():
    for game in range(1,11):
        input("Wanna play again?Enter Y or N")
        return choice == 'Y'

print("Welcome!! ...Let's roll on to the game-Tic-Tac-Toe")
while True:
    game_board = [' '] * 10
    User_symbol, Computer_symbol = player_input()
    turn = who_first()
    print(turn + ' will go first')
    game_initiater = input('Ready to play?Y or N: ').upper()
    if game_initiater == 'Y':
        begin_game = True
    else:
        begin_game = False

    while begin_game:
        game_winner = []
        if turn == 'User':
            print(display_board(game_board))
            position = player_choice(game_board)
            place_symbol(game_board, User_symbol, position)
            if win_check(game_board, User_symbol):
                print(display_board(game_board))
                game_winner.append(['User', User_symbol])
                print(f'User wins game {i}')
                begin_game = False
            else:

                if full_board_check(game_board):
                    print(display_board(game_board))
                    print("It's a Tie")
                    game_winner.append('Tie')
                    begin_game = False
                else:
                    turn = 'Computer'
        else:
            print(display_board(game_board))
            possible_choices = list(range(1, 10))
            position = random.choice(possible_choices)
            place_symbol(game_board, Computer_symbol, position)
            if win_check(game_board, Computer_symbol):
                print(display_board(game_board)
            game_winner.append(['Computer', Computer_symbol])
            print(f'Computer wins game{i}')
            begin_game = True

Enquiry=0
Enquiry=int(input('Enter the game number to get the information: ')
print('Winner of the round is ',+ game_winner[Enquiry-1])
















