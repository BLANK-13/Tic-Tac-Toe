import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
 
sign = 0
board = [[" " for x in range(3)] for y in range(3)]
 
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
 
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif(is_full()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")
 
def is_free(i, j):
    return board[i][j] == " "
def is_full():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
    
def ai():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]
 
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(is_full()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
        
    if(x):
        if sign % 2 != 0:
            move = ai()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
 
# Create the GUI of game board for play along with system
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 
# Initialize the game board to play with system
def with_ai(game_board):
    global board
    board = [[" " for x in range(3)] for y in range(3)]
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    e1 = Entry()
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text =  "Computer : O",
                width = 10, state = DISABLED)
     
    l2.grid(row = 2, column = 1)
    gameboard_pc(game_board, l1, l2)
 
# Initialize the game board to play with another player
def with_player(game_board):
    global board
    board = [[" " for x in range(3)] for y in range(3)]
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text = "Player 1 : X", width = 10)
     
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Player 2 : O",
                width = 10, state = DISABLED)
     
    l2.grid(row = 2, column = 1)
    gameboard_pl(game_board, l1, l2)
 
# main function
def play():
    menu = Tk()
    menu.geometry("250x150")
    menu.title("Tic Tac Toe")
    wpc = partial(with_ai, menu)
    wpl = partial(with_player, menu)
     
    head = Button(menu, text = "Tic Tac Toe GUI",
                  activeforeground = 'grey',
                  activebackground = "white", bg = "grey",
                  fg = "white", width = 500, font = 'summer', bd = 5)
     
    B1 = Button(menu, text = "Single Player", command = wpc,
                activeforeground = 'grey',
                activebackground = "white", bg = "grey",
                fg = "white", width = 500, font = 'summer', bd = 5)
     
    B2 = Button(menu, text = "Multi Player", command = wpl, activeforeground = 'grey',
                activebackground = "white", bg = "grey", fg = "white",
                width = 500, font = 'summer', bd = 5)
     
    B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'grey',
                activebackground = "white", bg = "grey", fg = "white",
                width = 500, font = 'summer', bd = 5)
    head.pack(side = 'top')
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()
 
# Call main function
if __name__ == '__main__':
    play()