from __future__ import print_function
import random
def setNewBoard():
    board=[]
    for i in range(8):
        board.append([' '] * 8)
    return board
    
def setDrawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+'
    print(HLINE)
    for y in range(6):
        print(y+1, end = " ")
        for x in range(7):
            print('| %s' % (board[x][y]), end = " ")
        print('|')
        print(HLINE)
    print('    1   2   3   4   5   6   7')
def isOnBoard(x, y):
    return x >= 0 and x <= 6 and y >= 0 and y <=5
def checkMove(board, tile, move):
    tilesToFlip = [ ]
    if move =='1':
        x,y = 0,6
    elif move == '2':
        x,y= 1,6
    elif move == '3':
        x,y =2,6
    elif move == '4':
        x,y = 3,6 
    elif move == '5':
        x,y = 4,6 
    elif move == '6':
        x,y = 5,6 
    elif move == '7':
        x,y = 6,6 
    if move != ' ':
        for xdirection, ydirection in [ [0, -1]]:  
            x += xdirection 
            y += ydirection 
            if board[x][y] !=' ':
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    continue
                while board[x][y] != ' ':
                    x += xdirection
                    y += ydirection
                    if not isOnBoard(x, y): 
                        break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == ' ':
                tilesToFlip.append([x, y ])
    if len(tilesToFlip) == 0: 
        return False   
    return tilesToFlip

def setMove(board, tile, move):
    tilesToFlip = checkMove(board, tile,move)
    if tilesToFlip == False:
        return False
    for x, y in tilesToFlip:
        board[x][y] = tile     
    return True

def getYourMove(board, YourTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7'.split()
    while True:
        move = raw_input('Enter your move <x,y>:')
        if  move in DIGITS1TO8 :
            if checkMove(board, YourTile, move) == False:
                print ("--")
                continue
            else:
                break
        else:
            print('--(1-8)')
    return move
def random1():
    A= ['1','2','3','4','5','6','7']
    return random.choice(['1','2','3','4','5','6','7'])
def getcommove(board,computerTile): 
    DIGITS1TO8 = '1 2 3 4 5 6 7'.split()
  
    while True:
        AI_pos = random1()
        if  AI_pos in DIGITS1TO8 :
           
            if checkMove(board, computerTile, AI_pos) == False:
                AI_pos = random1()
                print ("--")
                continue
            else:
                break
        else:
            print('--(1-8)')
    return AI_pos
    
def AI_Defending(board):
    global defending
    global AI_pos
    defending = False
    # horizontal
    if(board[0][5] == "X" and board[0][4] == "X" and  board[0][3] == "X")or (board[0][4] == "X" and board[0][3] == "X" and  board[0][2] == "X")or (board[0][3] == "X" and board[0][2] == "X" and  board[0][1] == "X"):
        AI_pos = '1'
        defending = True
    if(board[1][5] == "X" and board[1][4] == "X" and  board[1][3] == "X")or (board[1][4] == "X" and board[1][3] == "X" and  board[1][2] == "X")or (board[1][3] == "X" and board[1][2] == "X" and  board[1][1] == "X"):
        AI_pos = '2'
        defending = True
    if(board[2][5] == "X" and board[2][4] == "X" and  board[2][3] == "X")or (board[2][4] == "X" and board[2][3] == "X" and  board[2][2] == "X")or (board[2][3] == "X" and board[2][2] == "X" and  board[2][1] == "X"):
        AI_pos = '3'
        defending = True
    if(board[3][5] == "X" and board[3][4] == "X" and  board[3][3] == "X")or (board[3][4] == "X" and board[3][3] == "X" and  board[3][2] == "X")or (board[3][3] == "X" and board[3][2] == "X" and  board[3][1] == "X"):
        AI_pos = '4'
        defending = True
    if(board[4][5] == "X" and board[4][4] == "X" and  board[4][3] == "X")or (board[4][4] == "X" and board[4][3] == "X" and  board[4][2] == "X")or (board[4][3] == "X" and board[4][2] == "X" and  board[4][1] == "X"):
        AI_pos = '5'
        defending = True
    if(board[5][5] == "X" and board[5][4] == "X" and  board[5][3] == "X")or (board[5][4] == "X" and board[5][3] == "X" and  board[5][2] == "X")or (board[5][3] == "X" and board[5][2] == "X" and  board[5][1] == "X"):
        AI_pos = '6'
        defending = True
    if(board[6][5] == "X" and board[6][4] == "X" and  board[6][3] == "X")or (board[6][4] == "X" and board[6][3] == "X" and  board[6][2] == "X")or (board[6][3] == "X" and board[6][2] == "X" and  board[6][1] == "X"):
        AI_pos = '7'
        defending = True  
    
    # vertical
    
    if (board[1][5] == 'X' and board[2][5] == 'X' and board[3][5] == 'X' and board[0][5] == ' '):
            AI_pos =  '1'
            defending = True
    if (board[2][5] == 'X' and board[3][5] == 'X' and board[4][5] == 'X' and board[1][5] == ' '):
            AI_pos =  '2'
            defending = True
    if (board[3][5] == 'X' and board[4][5] == 'X' and board[5][5] == 'X' and board[2][5] == ' '):
            AI_pos =  '3'
            defending = True
    if (board[0][5] == 'X' and board[1][5] == 'X' and board[2][5] == 'X' and board[3][5] == ' '):
            AI_pos =  '4'
            defending = True
    if (board[4][5] == 'X' and board[5][5] == 'X' and board[6][5] == 'X' and board[3][5] == ' '):
            AI_pos =  '4'
            defending = True
    if (board[1][5] == 'X' and board[2][5] == 'X' and board[3][5] == 'X' and board[4][5] == ' '):
            AI_pos =  '5'
            defending = True
    if (board[2][5] == 'X' and board[3][5] == 'X' and board[4][5] == 'X' and board[5][5] == ' '):
            AI_pos =  '6'
            defending = True
    if (board[3][5] == 'X' and board[4][5] == 'X' and board[5][5] == 'X' and board[6][5] == ' '):
            AI_pos =  '7'
            defending = True 
    
    for y in range(5):
        y=y+1
        if (board[1][y-1] == 'X' and board[2][y-1] == 'X' and board[3][y-1] == 'X' and board[0][y-1] == ' '):
            if(board[0][y])!=' ':
                AI_pos =  '1'
                defending = True
        if (board[2][y-1] == 'X' and board[3][y-1] == 'X' and board[4][y-1] == 'X' and board[1][y-1] == ' '):
            if(board[1][y])!=' ':
                AI_pos =  '2'
                defending = True
        if (board[3][y-1] == 'X' and board[4][y-1] == 'X' and board[5][y-1] == 'X' and board[2][y-1] == ' '):
            if(board[2][y])!=' ':
                AI_pos =  '3'
                defending = True
        if (board[0][y-1] == 'X' and board[1][y-1] == 'X' and board[2][y-1] == 'X' and board[3][y-1] == ' '):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                defending = True
        if (board[4][y-1] == 'X' and board[5][y-1] == 'X' and board[6][y-1] == 'X' and board[3][y-1] == ' '):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                defending = True
        if (board[1][y-1] == 'X' and board[2][y-1] == 'X' and board[3][y-1] == 'X' and board[4][y-1] == ' '):
            if(board[4][y])!=' ':
                AI_pos =  '5'
                defending = True
        if (board[2][y-1] == 'X' and board[3][y-1] == 'X' and board[4][y-1] == 'X' and board[5][y-1] == ' '):
            if(board[5][y])!=' ':
                AI_pos =  '6'
                defending = True
        if (board[3][y-1] == 'X' and board[4][y-1] == 'X' and board[5][y-1] == 'X' and board[6][y-1] == ' '):
            if(board[6][y])!=' ': 
                AI_pos =  '7'
                defending = True  
                
    #R
    for y in range(3):
        if (board[1][y+2] == 'X' and board[2][y+1] == 'X' and board[3][y] == 'X' and board[0][y+3] == ' '):
            if(board[0][y+4]) != ' ':
                AI_pos =  '1'
                defending = True
        if (board[2][y+2] == 'X' and board[3][y+1] == 'X' and board[4][y] == 'X' and board[1][y+3] == ' '):
            if(board[1][y+4]) != ' ':
                AI_pos =  '2'
                defending = True
        if (board[3][y+2] == 'X' and board[4][y+1] == 'X' and board[5][y] == 'X' and board[2][y+3] == ' '):
            if(board[2][y+4]) != ' ':
                AI_pos =  '3'
                defending = True
        if (board[4][y+2] == 'X' and board[5][y+1] == 'X' and board[6][y] == 'X' and board[3][y+3] == ' '):
            if(board[3][y+4]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[0][y+3] == 'X' and board[1][y+2] == 'X' and board[2][y+1] == 'X' and board[3][y] == ' '):
            if(board[3][y+1]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[1][y+3] == 'X' and board[2][y+2] == 'X' and board[3][y+1] == 'X' and board[4][y] == ' '):
            if(board[4][y+1]) != ' ':
                AI_pos =  '5'
                defending = True
        if (board[2][y+3] == 'X' and board[3][y+2] == 'X' and board[4][y+1] == 'X' and board[5][y] == ' '):
            if(board[5][y+1]) != ' ':
                AI_pos =  '6'
                defending = True
        if (board[3][y+3] == 'X' and board[4][y+2] == 'X' and board[5][y+1] == 'X' and board[6][y] == ' '):
            if(board[6][y+1]) != ' ':
                AI_pos =  '7'
                defending = True      
    
    #L
    for y in range(3):
        y=y+1
        if (board[1][y] == 'X' and board[2][y+1] == 'X' and board[3][y+2] == 'X' and board[0][y-1] == ' '):
            if(board[0][y]) != ' ':
                AI_pos =  '1'
                defending = True
        if (board[2][y] == 'X' and board[3][y+1] == 'X' and board[4][y+2] == 'X' and board[1][y-1] == ' '):
            if(board[1][y]) != ' ':
                AI_pos =  '2'
                defending = True
        if (board[3][y] == 'X' and board[4][y+1] == 'X' and board[5][y+2] == 'X' and board[2][y-1] == ' '):
            if(board[2][y]) != ' ':
                AI_pos =  '3'
                defending = True
        if (board[4][y] == 'X' and board[5][y+1] == 'X' and board[6][y+2] == 'X' and board[3][y-1] == ' '):
            if(board[3][y]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[0][y-1] == 'X' and board[1][y] == 'X' and board[2][y+1] == 'X' and board[3][y+2] == ' '):
            if(board[3][y+3]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[1][y-1] == 'X' and board[2][y] == 'X' and board[3][y+1] == 'X' and board[4][y+2] == ' '):
            if(board[4][y+3]) != ' ':
                AI_pos =  '5'
                defending = True
        if (board[2][y-1] == 'X' and board[3][y] == 'X' and board[4][y+1] == 'X' and board[5][y+2] == ' '):
            if(board[5][y+3]) != ' ':
                AI_pos =  '6'
                defending = True
        if (board[3][y-1] == 'X' and board[4][y] == 'X' and board[5][y+1] == 'X' and board[6][y+2] == ' '):
            if(board[6][y+3]) != ' ':
                AI_pos =  '7'
                defending = True 
                
    #2
    if (board[0][5] == 'X' and board[1][5] == ' ' and board[2][5] == 'X' and board[3][5] == 'X'):
            AI_pos =  '2'
            defending = True
    if (board[1][5] == 'X' and board[2][5] == ' ' and board[3][5] == 'X' and board[4][5] == 'X'):
            AI_pos =  '3'
            defending = True
    if (board[2][5] == 'X' and board[3][5] == ' ' and board[4][5] == 'X' and board[5][5] == 'X'):
            AI_pos =  '4'
            defending = True
    if (board[3][5] == 'X' and board[4][5] == ' ' and board[5][5] == 'X' and board[6][5] == 'X'):
            AI_pos =  '5'
            defending = True                            
    
    for y in range(5):
        y=y+1
        if (board[0][y-1] == 'X' and board[1][y-1] == ' ' and board[2][y-1] == 'X' and board[3][y-1] == 'X'):
            if(board[1][y])!=' ':
                AI_pos =  '2'
                defending = True
        if (board[1][y-1] == 'X' and board[2][y-1] == ' ' and board[3][y-1] == 'X' and board[4][y-1] == 'X'):
            if(board[2][y])!=' ':
                AI_pos =  '3'
                defending = True
        if (board[2][y-1] == 'X' and board[3][y-1] == ' ' and board[4][y-1] == 'X' and board[5][y-1] == 'X'):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                defending = True
        if (board[3][y-1] == 'X' and board[4][y-1] == ' ' and board[5][y-1] == 'X' and board[6][y-1] == 'X'):
            if(board[4][y])!=' ':
                AI_pos =  '5'
                defending = True
                
    #2R
    for y in range(3):
        y=y+1
        if (board[0][y+2] == 'X' and board[1][y+1] == ' ' and board[2][y] == 'X' and board[3][y-1] == 'X'):
            if(board[1][y+2]) != ' ':
                AI_pos =  '2'
                defending = True
        if (board[1][y+2] == 'X' and board[2][y+1] == ' ' and board[3][y] == 'X' and board[4][y-1] == 'X'):
            if(board[2][y+2]) != ' ':
                AI_pos =  '3'
                defending = True
        if (board[2][y+2] == 'X' and board[3][y+1] == ' ' and board[4][y] == 'X' and board[5][y-1] == 'X'):
            if(board[3][y+2]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[3][y+2] == 'X' and board[4][y+1] == ' ' and board[5][y] == 'X' and board[6][y-1] == 'X'):
            if(board[4][y+2]) != ' ':
                AI_pos =  '5'
                defending = True
        
    #2L
    for y in range(3):
        if (board[0][y] == 'X' and board[1][y+1] == ' ' and board[2][y+2] == 'X' and board[3][y+3] == 'X'):
            if(board[1][y+2]) != ' ':
                AI_pos =  '2'
                defending = True
        if (board[1][y] == 'X' and board[2][y+1] == ' ' and board[3][y+2] == 'X' and board[4][y+3] == 'X'):
            if(board[2][y+2]) != ' ':
                AI_pos =  '3'
                defending = True
        if (board[2][y] == 'X' and board[3][y+1] == ' ' and board[4][y+2] == 'X' and board[5][y+3] == 'X'):
            if(board[3][y+2]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[3][y] == 'X' and board[4][y+1] == ' ' and board[5][y+2] == 'X' and board[6][y+3] == 'X'):
            if(board[4][y+2]) != ' ':
                AI_pos =  '5'
                defending = True
                
    #3
    if (board[0][5] == 'X' and board[1][5] == 'X' and board[2][5] == ' ' and board[3][5] == 'X'):
            AI_pos =  '3'
            defending = True
    if (board[1][5] == 'X' and board[2][5] == 'X' and board[3][5] == ' ' and board[4][5] == 'X'):
            AI_pos =  '4'
            defending = True
    if (board[2][5] == 'X' and board[3][5] == 'X' and board[4][5] == ' ' and board[5][5] == 'X'):
            AI_pos =  '5'
            defending = True
    if (board[3][5] == 'X' and board[4][5] == 'X' and board[5][5] == ' ' and board[6][5] == 'X'):
            AI_pos =  '6'
            defending = True
            
    for y in range(5):
        y=y+1
        if (board[0][y-1] == 'X' and board[1][y-1] == 'X' and board[2][y-1] == ' ' and board[3][y-1] == 'X'):
            if(board[2][y])!=' ':
                AI_pos =  '3'
                defending = True
        if (board[1][y-1] == 'X' and board[2][y-1] == 'X' and board[3][y-1] == ' ' and board[4][y-1] == 'X'):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                defending = True
        if (board[2][y-1] == 'X' and board[3][y-1] == 'X' and board[4][y-1] == ' ' and board[5][y-1] == 'X'):
            if(board[4][y])!=' ':
                AI_pos =  '5'
                defending = True
        if (board[3][y-1] == 'X' and board[4][y-1] == 'X' and board[5][y-1] == ' ' and board[6][y-1] == 'X'):
            if(board[5][y])!=' ':
                AI_pos =  '6'
                defending = True
            
    #3R
    for y in range(3):
        y=y+1
        if (board[0][y+2] == 'X' and board[1][y+1] == 'X' and board[2][y] == ' ' and board[3][y-1] == 'X'):
            if(board[2][y+1]) != ' ':
                AI_pos =  '3'
                defending = True
        if (board[1][y+2] == 'X' and board[2][y+1] == 'X' and board[3][y] == ' ' and board[4][y-1] == 'X'):
            if(board[3][y+1]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[2][y+2] == 'X' and board[3][y+1] == 'X' and board[4][y] == ' ' and board[5][y-1] == 'X'):
            if(board[4][y+1]) != ' ':
                AI_pos =  '5'
                defending = True
        if (board[3][y+2] == 'X' and board[4][y+1] == 'X' and board[5][y] == ' ' and board[6][y-1] == 'X'):
            if(board[5][y+1]) != ' ':
                AI_pos =  '6'
                defending = True
                
    #3L
    for y in range(3):
        if (board[0][y] == 'X' and board[1][y+1] == 'X' and board[2][y+2] == ' ' and board[3][y+3] == 'X'):
            if(board[2][y+3]) != ' ':
                AI_pos =  '3'
                defending = True
        if (board[1][y] == 'X' and board[2][y+1] == 'X' and board[3][y+2] == ' ' and board[4][y+3] == 'X'):
            if(board[3][y+3]) != ' ':
                AI_pos =  '4'
                defending = True
        if (board[2][y] == 'X' and board[3][y+1] == 'X' and board[4][y+2] == ' ' and board[5][y+3] == 'X'):
            if(board[4][y+3]) != ' ':
                AI_pos =  '5'
                defending = True
        if (board[3][y] == 'X' and board[4][y+1] == 'X' and board[5][y+2] == ' ' and board[6][y+3] == 'X'):
            if(board[5][y+3]) != ' ':
                AI_pos =  '6'
                defending = True
    
    return defending, AI_pos

    
def AI_Attacking(board):
    global attacking
    global AI_pos
    attacking = False
    if(board[3][5] == " " ) :
        AI_pos = '4'
        attacking = True

        
    # horizontal
    if (board[1][5] == 'O' and board[2][5] == 'O' and board[3][5] == 'O' and board[0][5] == ' '):
            AI_pos =  '1'
            attacking = True
    if (board[2][5] == 'O' and board[3][5] == 'O' and board[4][5] == 'O' and board[1][5] == ' '):
            AI_pos =  '2'
            attacking = True
    if (board[3][5] == 'O' and board[4][5] == 'O' and board[5][5] == 'O' and board[2][5] == ' '):
            AI_pos =  '3'
            attacking = True
    if (board[0][5] == 'O' and board[1][5] == 'O' and board[2][5] == 'O' and board[3][5] == ' '):
            AI_pos =  '4'
            attacking = True
    if (board[4][5] == 'O' and board[5][5] == 'O' and board[6][5] == 'O' and board[3][5] == ' '):
            AI_pos =  '4'
            attacking = True
    if (board[1][5] == 'O' and board[2][5] == 'O' and board[3][5] == 'O' and board[4][5] == ' '):
            AI_pos =  '5'
            attacking = True
    if (board[2][5] == 'O' and board[3][5] == 'O' and board[4][5] == 'O' and board[5][5] == ' '):
            AI_pos =  '6'
            attacking = True
    if (board[3][5] == 'O' and board[4][5] == 'O' and board[5][5] == 'O' and board[6][5] == ' '):
            AI_pos =  '7'
            attacking = True
    
    for y in range(5):
        y=y+1
        if (board[1][y-1] == 'O' and board[2][y-1] == 'O' and board[3][y-1] == 'O' and board[0][y-1] == ' '):
            if(board[0][y])!=' ':
                AI_pos =  '1'
                attacking = True
        if (board[2][y-1] == 'O' and board[3][y-1] == 'O' and board[4][y-1] == 'O' and board[1][y-1] == ' '):
            if(board[1][y])!=' ':
                AI_pos =  '2'
                attacking = True
        if (board[3][y-1] == 'O' and board[4][y-1] == 'O' and board[5][y-1] == 'O' and board[2][y-1] == ' '):
            if(board[2][y])!=' ':
                AI_pos =  '3'
                attacking = True
        if (board[0][y-1] == 'O' and board[1][y-1] == 'O' and board[2][y-1] == 'O' and board[3][y-1] == ' '):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                attacking = True
        if (board[4][y-1] == 'O' and board[5][y-1] == 'O' and board[6][y-1] == 'O' and board[3][y-1] == ' '):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                attacking = True
        if (board[1][y-1] == 'O' and board[2][y-1] == 'O' and board[3][y-1] == 'O' and board[4][y-1] == ' '):
            if(board[4][y])!=' ':
                AI_pos =  '5'
                attacking = True
        if (board[2][y-1] == 'O' and board[3][y-1] == 'O' and board[4][y-1] == 'O' and board[5][y-1] == ' '):
            if(board[5][y])!=' ':
                AI_pos =  '6'
                attacking = True
        if (board[3][y-1] == 'O' and board[4][y-1] == 'O' and board[5][y-1] == 'O' and board[6][y-1] == ' '):
            if(board[6][y])!=' ': 
                AI_pos =  '7'
                attacking = True
    
    # Tung    
    if (board[0][5] == 'O' and board[0][4] == 'O' and board[0][3] == 'O' and board[0][2] == ' ')or (board[0][4] == 'O' and board[0][3] == 'O' and board[0][2] == 'O' and board[0][1] == ' ')or(board[0][3] == 'O' and board[0][2] == 'O' and board[0][1] == 'O' and board[0][0] == ' '):
            AI_pos =  '1'
            attacking = True
    if (board[1][5] == 'O' and board[1][4] == 'O' and board[1][3] == 'O' and board[1][2] == ' ')or (board[1][4] == 'O' and board[1][3] == 'O' and board[1][2] == 'O' and board[1][1] == ' ')or(board[1][3] == 'O' and board[1][2] == 'O' and board[1][1] == 'O' and board[1][0] == ' '):
            AI_pos =  '2'
            attacking = True
    if (board[2][5] == 'O' and board[2][4] == 'O' and board[2][3] == 'O' and board[2][2] == ' ')or (board[2][4] == 'O' and board[2][3] == 'O' and board[2][2] == 'O' and board[2][1] == ' ')or(board[2][3] == 'O' and board[2][2] == 'O' and board[2][1] == 'O' and board[2][0] == ' '):
            AI_pos =  '3'
            attacking = True
    if (board[3][5] == 'O' and board[3][4] == 'O' and board[3][3] == 'O' and board[3][2] == ' ')or (board[3][4] == 'O' and board[3][3] == 'O' and board[3][2] == 'O' and board[3][1] == ' ')or(board[3][3] == 'O' and board[3][2] == 'O' and board[3][1] == 'O' and board[3][0] == ' '):
            AI_pos =  '4'
            attacking = True
    if (board[4][5] == 'O' and board[4][4] == 'O' and board[4][3] == 'O' and board[4][2] == ' ')or (board[4][4] == 'O' and board[4][3] == 'O' and board[4][2] == 'O' and board[4][1] == ' ')or(board[4][3] == 'O' and board[4][2] == 'O' and board[4][1] == 'O' and board[4][0] == ' '):
            AI_pos =  '5'
            attacking = True
    if (board[5][5] == 'O' and board[5][4] == 'O' and board[5][3] == 'O' and board[5][2] == ' ')or (board[5][4] == 'O' and board[5][3] == 'O' and board[5][2] == 'O' and board[5][1] == ' ')or(board[5][3] == 'O' and board[5][2] == 'O' and board[5][1] == 'O' and board[5][0] == ' '):
            AI_pos =  '6'
            attacking = True
    if (board[6][5] == 'O' and board[6][4] == 'O' and board[6][3] == 'O' and board[6][2] == ' ')or (board[6][4] == 'O' and board[6][3] == 'O' and board[6][2] == 'O' and board[6][1] == ' ')or(board[6][3] == 'O' and board[6][2] == 'O' and board[6][1] == 'O' and board[6][0] == ' '):
            AI_pos =  '7'
            attacking = True
    
            
    #R
    for y in range(3):
        if (board[1][y+2] == 'O' and board[2][y+1] == 'O' and board[3][y] == 'O' and board[0][y+3] == ' '):
            if(board[0][y+4]) != ' ':
                AI_pos =  '1'
                attacking = True
        if (board[2][y+2] == 'O' and board[3][y+1] == 'O' and board[4][y] == 'O' and board[1][y+3] == ' '):
            if(board[1][y+4]) != ' ':
                AI_pos =  '2'
                attacking = True
        if (board[3][y+2] == 'O' and board[4][y+1] == 'O' and board[5][y] == 'O' and board[2][y+3] == ' '):
            if(board[2][y+4]) != ' ':
                AI_pos =  '3'
                attacking = True
        if (board[4][y+2] == 'O' and board[5][y+1] == 'O' and board[6][y] == 'O' and board[3][y+3] == ' '):
            if(board[3][y+4]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[0][y+3] == 'O' and board[1][y+2] == 'O' and board[2][y+1] == 'O' and board[3][y] == ' '):
            if(board[3][y+1]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[1][y+3] == 'O' and board[2][y+2] == 'O' and board[3][y+1] == 'O' and board[4][y] == ' '):
            if(board[4][y+1]) != ' ':
                AI_pos =  '5'
                attacking = True
        if (board[2][y+3] == 'O' and board[3][y+2] == 'O' and board[4][y+1] == 'O' and board[5][y] == ' '):
            if(board[5][y+1]) != ' ':
                AI_pos =  '6'
                attacking = True
        if (board[3][y+3] == 'O' and board[4][y+2] == 'O' and board[5][y+1] == 'O' and board[6][y] == ' '):
            if(board[6][y+1]) != ' ':
                AI_pos =  '7'
                attacking = True
        
    
    #L
    for y in range(3):
        y=y+1
        if (board[1][y] == 'O' and board[2][y+1] == 'O' and board[3][y+2] == 'O' and board[0][y-1] == ' '):
            if(board[0][y]) != ' ':
                AI_pos =  '1'
                attacking = True
        if (board[2][y] == 'O' and board[3][y+1] == 'O' and board[4][y+2] == 'O' and board[1][y-1] == ' '):
            if(board[1][y]) != ' ':
                AI_pos =  '2'
                attacking = True
        if (board[3][y] == 'O' and board[4][y+1] == 'O' and board[5][y+2] == 'O' and board[2][y-1] == ' '):
            if(board[2][y]) != ' ':
                AI_pos =  '3'
                attacking = True
        if (board[4][y] == 'O' and board[5][y+1] == 'O' and board[6][y+2] == 'O' and board[3][y-1] == ' '):
            if(board[3][y]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[0][y-1] == 'O' and board[1][y] == 'O' and board[2][y+1] == 'O' and board[3][y+2] == ' '):
            if(board[3][y+3]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[1][y-1] == 'O' and board[2][y] == 'O' and board[3][y+1] == 'O' and board[4][y+2] == ' '):
            if(board[4][y+3]) != ' ':
                AI_pos =  '5'
                attacking = True
        if (board[2][y-1] == 'O' and board[3][y] == 'O' and board[4][y+1] == 'O' and board[5][y+2] == ' '):
            if(board[5][y+3]) != ' ':
                AI_pos =  '6'
                attacking = True
        if (board[3][y-1] == 'O' and board[4][y] == 'O' and board[5][y+1] == 'O' and board[6][y+2] == ' '):
            if(board[6][y+3]) != ' ':
                AI_pos =  '7'
                attacking = True
                
    #2
    if (board[0][5] == 'O' and board[1][5] == ' ' and board[2][5] == 'O' and board[3][5] == 'O'):
            AI_pos =  '2'
            attacking = True
    if (board[1][5] == 'O' and board[2][5] == ' ' and board[3][5] == 'O' and board[4][5] == 'O'):
            AI_pos =  '3'
            attacking = True
    if (board[2][5] == 'O' and board[3][5] == ' ' and board[4][5] == 'O' and board[5][5] == 'O'):
            AI_pos =  '4'
            attacking = True
    if (board[3][5] == 'O' and board[4][5] == ' ' and board[5][5] == 'O' and board[6][5] == 'O'):
            AI_pos =  '5'
            attacking = True
    
            
    for y in range(5):
        y=y+1
        if (board[0][y-1] == 'O' and board[1][y-1] == ' ' and board[2][y-1] == 'O' and board[3][y-1] == 'O'):
            if(board[1][y])!=' ':
                AI_pos =  '2'
                attacking = True
        if (board[1][y-1] == 'O' and board[2][y-1] == ' ' and board[3][y-1] == 'O' and board[4][y-1] == 'O'):
            if(board[2][y])!=' ':
                AI_pos =  '3'
                attacking = True
        if (board[2][y-1] == 'O' and board[3][y-1] == ' ' and board[4][y-1] == 'O' and board[5][y-1] == 'O'):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                attacking = True
        if (board[3][y-1] == 'O' and board[4][y-1] == ' ' and board[5][y-1] == 'O' and board[6][y-1] == 'O'):
            if(board[4][y])!=' ':
                AI_pos =  '5'
                attacking = True
    
    #3
    if (board[0][5] == 'O' and board[1][5] == 'O' and board[2][5] == ' ' and board[3][5] == 'O'):
            AI_pos =  '3'
            attacking = True
    if (board[1][5] == 'O' and board[2][5] == 'O' and board[3][5] == ' ' and board[4][5] == 'O'):
            AI_pos =  '4'
            attacking = True
    if (board[2][5] == 'O' and board[3][5] == 'O' and board[4][5] == ' ' and board[5][5] == 'O'):
            AI_pos =  '5'
            attacking = True
    if (board[3][5] == 'O' and board[4][5] == 'O' and board[5][5] == ' ' and board[6][5] == 'O'):
            AI_pos =  '6'
            attacking = True
    
            
    for y in range(5):
        y=y+1
        if (board[0][y-1] == 'O' and board[1][y-1] == 'O' and board[2][y-1] == ' ' and board[3][y-1] == 'O'):
            if(board[2][y])!=' ':
                AI_pos =  '3'
                attacking = True
        if (board[1][y-1] == 'O' and board[2][y-1] == 'O' and board[3][y-1] == ' ' and board[4][y-1] == 'O'):
            if(board[3][y])!=' ':
                AI_pos =  '4'
                attacking = True
        if (board[2][y-1] == 'O' and board[3][y-1] == 'O' and board[4][y-1] == ' ' and board[5][y-1] == 'O'):
            if(board[4][y])!=' ':
                AI_pos =  '5'
                attacking = True
        if (board[3][y-1] == 'O' and board[4][y-1] == 'O' and board[5][y-1] == ' ' and board[6][y-1] == 'O'):
            if(board[5][y])!=' ':
                AI_pos =  '6'
                attacking = True
                
    #2R
    for y in range(3):
        y=y+1
        if (board[0][y+2] == 'O' and board[1][y+1] == ' ' and board[2][y] == 'O' and board[3][y-1] == 'O'):
            if(board[1][y+2]) != ' ':
                AI_pos =  '2'
                attacking = True
        if (board[1][y+2] == 'O' and board[2][y+1] == ' ' and board[3][y] == 'O' and board[4][y-1] == 'O'):
            if(board[2][y+2]) != ' ':
                AI_pos =  '3'
                attacking = True
        if (board[2][y+2] == 'O' and board[3][y+1] == ' ' and board[4][y] == 'O' and board[5][y-1] == 'O'):
            if(board[3][y+2]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[3][y+2] == 'O' and board[4][y+1] == ' ' and board[5][y] == 'O' and board[6][y-1] == 'O'):
            if(board[4][y+2]) != ' ':
                AI_pos =  '5'
                attacking = True
        
    #2L
    for y in range(3):
        if (board[0][y] == 'O' and board[1][y+1] == ' ' and board[2][y+2] == 'O' and board[3][y+3] == 'O'):
            if(board[1][y+2]) != ' ':
                AI_pos =  '2'
                attacking = True
        if (board[1][y] == 'O' and board[2][y+1] == ' ' and board[3][y+2] == 'O' and board[4][y+3] == 'O'):
            if(board[2][y+2]) != ' ':
                AI_pos =  '3'
                attacking = True
        if (board[2][y] == 'O' and board[3][y+1] == ' ' and board[4][y+2] == 'O' and board[5][y+3] == 'O'):
            if(board[3][y+2]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[3][y] == 'O' and board[4][y+1] == ' ' and board[5][y+2] == 'O' and board[6][y+3] == 'O'):
            if(board[4][y+2]) != ' ':
                AI_pos =  '5'
                attacking = True
                
    #3R
    for y in range(3):
        y=y+1
        if (board[0][y+2] == 'O' and board[1][y+1] == 'O' and board[2][y] == ' ' and board[3][y-1] == 'O'):
            if(board[2][y+1]) != ' ':
                AI_pos =  '3'
                attacking = True
        if (board[1][y+2] == 'O' and board[2][y+1] == 'O' and board[3][y] == ' ' and board[4][y-1] == 'O'):
            if(board[3][y+1]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[2][y+2] == 'O' and board[3][y+1] == 'O' and board[4][y] == ' ' and board[5][y-1] == 'O'):
            if(board[4][y+1]) != ' ':
                AI_pos =  '5'
                attacking = True
        if (board[3][y+2] == 'O' and board[4][y+1] == 'O' and board[5][y] == ' ' and board[6][y-1] == 'O'):
            if(board[5][y+1]) != ' ':
                AI_pos =  '6'
                attacking = True
                
    #3L
    for y in range(3):
        if (board[0][y] == 'O' and board[1][y+1] == 'O' and board[2][y+2] == ' ' and board[3][y+3] == 'O'):
            if(board[2][y+3]) != ' ':
                AI_pos =  '3'
                attacking = True
        if (board[1][y] == 'O' and board[2][y+1] == 'O' and board[3][y+2] == ' ' and board[4][y+3] == 'O'):
            if(board[3][y+3]) != ' ':
                AI_pos =  '4'
                attacking = True
        if (board[2][y] == 'O' and board[3][y+1] == 'O' and board[4][y+2] == ' ' and board[5][y+3] == 'O'):
            if(board[4][y+3]) != ' ':
                AI_pos =  '5'
                attacking = True
        if (board[3][y] == 'O' and board[4][y+1] == 'O' and board[5][y+2] == ' ' and board[6][y+3] == 'O'):
            if(board[5][y+3]) != ' ':
                AI_pos =  '6'
                attacking = True
        
    
    return attacking, AI_pos
def win (board):
    # horizontal
    for y in range(6):
        winning = []
        for x in range(7):
            if board[x-1][y-1] != 'A':
                winning.append([board[x][y]])
        if len(winning) > 3:
            for i in range(6):
                if winning[i-1]==['X'] and winning[i]==['X'] and winning[i+1]==['X'] and winning[i+2]==['X']:
                    return True
                if winning[i-1]==['O'] and winning[i]==['O'] and winning[i+1]==['O'] and winning[i+2]==['O']:
                    return True                   
        else:
            winning = []
            return False

    # vertical
    for x in range(7):
        winning = []
        for y in range(6):
            if board[x][y] != 'A':
                winning.append([board[x][y]])
        if len(winning) > 3:
            for i in range(4):
                if (winning[i-1]==['X'] and winning[i]==['X'] and winning[i+1]==['X'] and winning[i+2]==['X']):
                    return True
                if (winning[i-1]==['O'] and winning[i]==['O'] and winning[i+1]==['O'] and winning[i+2]==['O']):
                    return True                  
        else:
            return False
    
    if (board[0][3]=='X' and board[1][2]=='X' and board[2][1]=='X'and board[3][0]=='X'):
        return True
    if (board[0][3]=='O' and board[1][2]=='O' and board[2][1]=='O'and board[3][0]=='O'):
        return True
    
    A=[[0,5],[ 1,4],[ 2,3],[ 3,2],[ 4,1],[ 5,0]]
    winning = []
    for x,y in A:
        winning.append([board[x][y]])
    if len(winning) > 3:
            for i in range(4):
                if (winning[i-1]==['X'] and winning[i]==['X'] and winning[i+1]==['X'] and winning[i+2]==['X']):
                    return True
                if (winning[i-1]==['O'] and winning[i]==['O'] and winning[i+1]==['O'] and winning[i+2]==['O']):
                    return True  
        
        
        
    return False
   
def GoFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'Your'
while True:
        mainBoard = setNewBoard()
        YourTile, computerTile = "X","O" 
        turn = GoFirst()
        print('The ' + turn + ' will go first.')
        while True:
            if turn == 'Your':
                setDrawBoard(mainBoard)
                move = getYourMove(mainBoard, YourTile)
                setMove(mainBoard, YourTile, move)
                if win(mainBoard) == True :
                    break
                turn = 'computer'
                print ("--Your Move--")
            else :
                setDrawBoard(mainBoard)
                AI_pos = int
                attacking = False
                defending = False
                AI_Attacking(mainBoard)
                if attacking == True:
                    setMove(mainBoard, computerTile, AI_pos)
                  
                elif attacking == False:
                    AI_Defending(mainBoard)
                    if defending == True:
                        setMove(mainBoard, computerTile, AI_pos)
                    
                    elif  defending == False:
                        AI_pos = getcommove(mainBoard, computerTile)
                        setMove(mainBoard, computerTile,AI_pos)
                        
                if win(mainBoard) == True :
                    break
                turn = 'Your'
                print ("--computer Move--")
                print ('com move --> ',AI_pos)

        setDrawBoard(mainBoard)
        print (turn,' win ')
        break
                
                
                
                
                
