import random
import time
from ast import While

game_list : list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

class Player():
    def __init__(self, name : str, x_or_o : str, first : bool) -> None:
        self.name = name
        self.x_or_o = x_or_o
        self.first = first
        self.player_choice = []
        
    def move(self, square : int):
        self.player_choice.append(square)
        self.show_board(square)
                    
    def show_board(self, player_move : int):
        global game_list
        game_list[player_move-1] = self.x_or_o
        print()
        print(f'{game_list[0]} | {game_list[1]} | {game_list[2]}\n{game_list[3]} | {game_list[4]} | {game_list[5]}\n{game_list[6]} | {game_list[7]} | {game_list[8]}')
        print(end='\n\n')
        
    # attributes
    name:str
    x_or_o:str
    player_choice:list
    first:bool
    winner:bool = False

    
    

def win_tie_check(player_1: Player, player_2 : Player):
    winning_values = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for values in winning_values:
        if set(values).issubset(set(player_1.player_choice)):
            player_1.winner = True
            break
        if set(values).issubset(set(player_2.player_choice)):
            player_2.winner = True
            break
    


def intro():
    print('Welcomce to tic tac toe game !\n\nBoard template\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n')


def game_logic(solo : bool, player_1 : Player, player_2 : Player):
    tie_counter = 0
    player_1_turn = player_1.first
    
    if solo: #solo logic
        while True:    
            if player_1_turn:
                while True:
                    try:
                        move = int(input(f'please enter your move {player_1.name} - 1 to 9 -\n'))
                        if game_list[move-1] == ' ':
                            player_1.move(move)
                            break
                        else:
                            print(f'{move} is already chosen try again\n') 
                    except:
                        print(' please enter a choice from 1 to 9\n')
                        continue
                player_1_turn = False
            else:
                # this is a terrible way of doing a hard AI but I'm too lazy to implement the minimax algo, plus this feels more human it's hard enough but not impossible its like playing with a 9 years old lol.
                counter:int = 0
                while True:
                    if 1 in player_1.player_choice and 2 in player_1.player_choice and counter < 3:
                        move = 3
                        counter+= 1
                    elif 2 in player_1.player_choice and 3 in player_1.player_choice and counter < 3:
                        move = 1
                        counter+= 1
                    elif 1 in player_1.player_choice and 3 in player_1.player_choice and counter < 3:
                        move = 2
                        counter+= 1
                    elif 4 in player_1.player_choice and 5 in player_1.player_choice and counter < 3:
                        move = 6
                        counter+= 1
                    elif 5 in player_1.player_choice and 6 in player_1.player_choice and counter < 12:
                        move = 4
                        counter+= 1
                    elif 4 in player_1.player_choice and 6 in player_1.player_choice and counter < 12:
                        move = 5
                        counter+= 1
                    elif 7 in player_1.player_choice and 8 in player_1.player_choice and counter < 12:
                        move = 9
                        counter+= 1
                    elif 7 in player_1.player_choice and 9 in player_1.player_choice and counter < 12:
                        move = 8
                        counter+= 1
                    elif 8 in player_1.player_choice and 9 in player_1.player_choice and counter < 12:
                        move = 7
                        counter+= 1
                    elif 1 in player_1.player_choice and 4 in player_1.player_choice and counter < 12:
                        move = 7
                        counter+= 1
                    elif 1 in player_1.player_choice and 7 in player_1.player_choice and counter < 12:
                        move = 4
                        counter+= 1
                    elif 4 in player_1.player_choice and 7 in player_1.player_choice and counter < 12:
                        move = 1
                        counter+= 1
                    elif 2 in player_1.player_choice and 5 in player_1.player_choice and counter < 12:
                        move = 8
                        counter+= 1
                    elif 2 in player_1.player_choice and 8 in player_1.player_choice and counter < 12:
                        move = 5
                        counter+= 1
                    elif 5 in player_1.player_choice and 8 in player_1.player_choice and counter < 12:
                        move = 2
                        counter+= 1
                    elif 3 in player_1.player_choice and 6 in player_1.player_choice and counter < 12:
                        move = 9
                        counter+= 1
                    elif 3 in player_1.player_choice and 9 in player_1.player_choice and counter < 12:
                        move = 6
                        counter+= 1
                    elif 9 in player_1.player_choice and 6 in player_1.player_choice and counter < 12:
                        move = 3
                        counter+= 1
                    elif 1 in player_1.player_choice and 5 in player_1.player_choice and counter < 12:
                        move = 9
                        counter+= 1
                    elif 5 in player_1.player_choice and 9 in player_1.player_choice and counter < 12:
                        move = 1
                        counter+= 1
                    elif 1 in player_1.player_choice and 9 in player_1.player_choice and counter < 12:
                        move = 5
                        counter+= 1
                    elif 3 in player_1.player_choice and 5 in player_1.player_choice and counter < 12:
                        move = 7
                        counter+= 1
                    elif 3 in player_1.player_choice and 7 in player_1.player_choice and counter < 12:
                        move = 5
                        counter+= 1
                    elif 5 in player_1.player_choice and 7 in player_1.player_choice and counter < 12:
                        move = 3
                        counter+= 1
                    else:
                        move = random.randint(1,9)
                    # [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
                    if move in player_1.player_choice or move in player_2.player_choice:
                        continue
                    else:
                        time.sleep(1)
                        player_2.move(move)
                        player_1_turn = True
                        break
                    
            win_tie_check(player_1= player_1, player_2= player_2) # check win status after each turn.
            tie_counter += 1 # keep track of turn to detect ties.
            if tie_counter == 9:
                print('it is a tie !\n')
                break
            if player_1.winner:
                print(f'{player_1.name} has WON !!\n')
                break
            if player_2.winner:
                print(f'{player_2.name} has WON on random mode xD\n')
                break
    else: # two players logic
        while True:    
            if player_1_turn:
                while True:
                    try:
                        move = int(input(f'please enter your move {player_1.name} - 1 to 9 -\n'))
                        if game_list[move-1] == ' ':
                            player_1.move(move)
                            break
                        else:
                            print(f'{move} is already chosen try again\n') 
                    except:
                        print(' please enter a choice from 1 to 9\n')
                        continue
                player_1_turn = False
            else:
                while True:
                    try:
                        move = int(input(f'please enter your move {player_2.name} - 1 to 9 -\n'))
                        if game_list[move-1] == ' ':
                            player_2.move(move)
                            break
                        else:
                            print(f'{move} is already chosen try again\n') 
                    except:
                            print(' please enter a choice from 1 to 9\n')
                            continue
                player_1_turn = True
                    
            win_tie_check(player_1= player_1, player_2= player_2) # check win status after each turn.
            tie_counter += 1 # keep track of turn to detect ties.
            if tie_counter == 9:
                print('it is a tie !\n')
                break
            if player_1.winner:
                print(f'{player_1.name} has WON !!\n')
                break
            if player_2.winner:
                print(f'{player_2.name} has WON !!\n')
                break
    

def tic_tac_toe():
    intro()
    
    global game_list
    solo : bool
    while True:
        solo_or_two = input('Do you wish to play alone or with someone? - press 1 for solo or press 2 to play with a friend.\n')
        if solo_or_two == '1':
            solo = True
            break
        elif solo_or_two == '2':
            solo = False
            break
        else:
            print('Wrong input please try again with either 1 or 2.\n')
            continue
    if solo:
        name = input("Hello please enter your name\n")
        while True:
            first = input('Do you wish to go first ? - press y / n\n')
            if first == 'y':
                while True:
                    x_or_o = input('Do you wish to choose x or o ? - press x / o\n')
                    if x_or_o == 'x':
                        player_1 = Player(name= name,first=True, x_or_o = x_or_o)
                        player_machine = Player(name = 'Machine',first=False, x_or_o = 'o')
                    elif x_or_o == 'o':
                        player_1 = Player(name= name,first=True, x_or_o = x_or_o)
                        player_machine = Player(name = 'Machine',first=False, x_or_o = 'x')
                    else:
                        print('please choose x or o\n')
                        continue
                    break
            elif first == 'n':
                while True:
                    x_or_o = input('Do you wish to choose x or o ? - press x / o\n')
                    if x_or_o == 'x':
                        player_1 = Player(name= name,first=False, x_or_o = x_or_o)
                        player_machine = Player(name = 'Machine',first=True, x_or_o = 'o')
                    elif x_or_o == 'o':
                        player_1 = Player(name= name,first=False, x_or_o = x_or_o)
                        player_machine = Player(name = 'Machine',first=True, x_or_o = 'x')
                    else:
                        print('please choose x or o\n')
                        continue
                    break
            else:
                print('please choose first as y or second as n\n')
                continue
            
            game_logic(solo= True, player_1= player_1, player_2= player_machine)
            if input('Do you want to play again? - y/n -\n') == 'y':
                game_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
            else:
                break
    else: # if there are two players.
        name_1 = input("Hello please enter your name \n")
        name_2 = input("\nHello friend please enter your name too \n")
        
        while True:
            print()
            first = input(f'{name_1} Do you wish to go first ? - press y / n\n')
            print()
            if first == 'y':
                while True:
                    x_or_o = input(f'{name_1} Do you wish to choose x or o ? - press x / o\n')
                    if x_or_o == 'x':
                        player_1 = Player(name= name_1,first=True, x_or_o = x_or_o)
                        player_2 = Player(name= name_2,first=False, x_or_o = 'o')
                    elif x_or_o == 'o':
                        player_1 = Player(name= name_1,first=True, x_or_o = x_or_o)
                        player_2 = Player(name= name_2,first=False, x_or_o = 'x')
                    else:
                        print('please choose x or o\n')
                        continue
                    print(f'\n{player_1.name} is {player_1.x_or_o}  ||  {player_2.name} is {player_2.x_or_o}\n')
                    break
            elif first == 'n': # if player 1 chooses to play 2nd.
                while True:
                    x_or_o = input(f'{name_1} Do you wish to choose x or o ? - press x / o\n')
                    if x_or_o == 'x':
                        player_1 = Player(name= name_1,first=False, x_or_o = x_or_o)
                        player_2 = Player(name= name_2,first=True, x_or_o = 'o')
                    elif x_or_o == 'o':
                        player_1 = Player(name= name_1,first=False, x_or_o = x_or_o)
                        player_2 = Player(name= name_2,first=True, x_or_o = 'x')
                    else:
                        print('please choose x or o\n')
                        continue
                    print(f'\n{player_1.name} is {player_1.x_or_o}  ||  {player_2.name} is {player_2.x_or_o}\n')
                    break
            else:
                print('please choose first as y or second as n\n')
                
            game_logic(solo= False, player_1= player_1, player_2= player_2)
            if input('Do you want to play again? - y/n -\n') == 'y':
                game_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
            else:
                break
                
        
    
    
tic_tac_toe()
