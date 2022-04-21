#Connect 4 game
#This game is played by 2 players
#Players choose a symbol, either X or O. 
#Each player in his turn drop his symbol from top of the board to the bottom
#The first player to connect 4 symbols horizontally, vertically or diagonally wins.
#Author:Habiba Alaa Mohamed Ali El-Behairy
#Date:28-2-2022
#version:1.0
rows=6
columns=7
board = [[' ' for  i in range(columns)] for j in range(rows)]
player1="X"
player2="O"

def bodyshape (rows,columns):#build board
    for i in range (columns): #each element in columns
        print(f" ({i+1}) ", end="") #Number of columns
    print("\n")
    for eachrow in (board):#eachrow in board
        print(eachrow)      

def horizontalwinning(player1,player2):#check for horizontal win
    for j in range (rows): #in each row
        for i in range (columns-3):#check each element in row if there is 4 connected horizontally
            if board[j][i]==board[j][i+1]== player1 and board[j][i+2]==board[j][i+3]==player1:
                print("X wins in horizontal way")
                return True
            if board[j][i]==board[j][i+1]== player2 and board[j][i+2]==board[j][i+3]==player2:
                print("O wins in horizontal way")
                return True

def verticalwinning(player1,player2):#check for vertival win
    for i in range (columns): #in each columns
        for j in range (rows-3):#check each element in column if there is 4 connected vertically
            if board[j][i]==board[j+1][i]== player1 and board[j+2][i]==board[j+3][i]==player1:
                print("X wins in vertical way")
                return True
            if board[j][i]==board[j+1][i]== player2 and board[j+2][i]==board[j+3][i]==player2:
                print("O wins in vertical way")
                return True

def diagonalwinning(piece):#check for diagonal win
    for i in range(columns-3):#in each 4 columns
        for j in range(rows-3):#check each elements in the 4 rows of columns if there is 4 connected in diagonal way
            if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
                print(piece,"wins in diagonal way")
                return True
    for i in range(columns-3):#in each 4 columns
        for j in range(3, rows):#check each elements starting from third row of columns if there is 4 connected in diagonal way
            if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
                print(piece,"wins in diagonal way")
                return True

def gamedraw():#check if game draw
    i=0
    for rows in board:#each row in board
        for eachelement in rows:#check each element and if its empty or not
            if eachelement==' ':
                i+=1
    if i==0:
        print("The game is draw")#if all elements are full and there is no winner ther game draw
        return True

def checkwinner():#check winner
    if horizontalwinning(player1,player2) or verticalwinning (player1,player2) or diagonalwinning (player1) or diagonalwinning(player2):
        return True

def methodofplaying(board,rows,columns):#how to play
    player=1
    while(True):
        bodyshape(rows,columns)
        if checkwinner():
            break
        if gamedraw():
            break
        chosencolumn= int(input('please choose columns from 1 to 7: '))#Column which player choose to drop his piece
        if chosencolumn<1 or chosencolumn>7:
            while (True):
                if chosencolumn<1 or chosencolumn>7 :
                   chosencolumn= int(input('wrong input, please choose columns from 1 to 7: '))
                else:
                    break
        for i in range (rows-1,-1,-1): #to start from the bottom and let the pieces droped to bottom 
            if player==1:
                if board[i][chosencolumn-1]==' ': #to see which index of the chosen column is empty
                    board[i][chosencolumn-1]="X" #fill the empty index with the piece of player 1
                    player=2 #player 2 turn
                    break
            else:
                if board[i][chosencolumn-1]==' ': #to see which index of the chosen column is empty
                    board[i][chosencolumn-1]="O" #fill the empty index with the piece of player 2
                    player=1 #player 1 turn
                    break

methodofplaying(board,rows,columns)
