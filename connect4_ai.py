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
    if(board[0][5] == "X" and board[0][4] == "X" ) or (board[0][5] == "X" and board[0][4] == "X" and  board[0][3] == "X")or (board[0][4] == "X" and board[0][3] == "X" and  board[0][2] == "X"):
        AI_pos = '1'
        defending = True
    if(board[1][5] == "X" and board[1][4] == "X" ) or (board[1][5] == "X" and board[1][4] == "X" and  board[1][3] == "X")or (board[1][4] == "X" and board[1][3] == "X" and  board[1][2] == "X"):
        AI_pos = '2'
        defending = True
    if(board[2][5] == "X" and board[2][4] == "X" )or (board[2][5] == "X" and board[2][4] == "X" and  board[2][3] == "X")or (board[2][4] == "X" and board[2][3] == "X" and  board[2][2] == "X"):
        AI_pos = '3'
        defending = True
    if(board[3][5] == "X" and board[3][4] == "X" )or (board[3][5] == "X" and board[3][4] == "X" and  board[3][3] == "X")or (board[3][4] == "X" and board[3][3] == "X" and  board[3][2] == "X"):
        AI_pos = '4'
        defending = True
    if(board[4][5] == "X" and board[4][4] == "X" )or (board[4][5] == "X" and board[4][4] == "X" and  board[4][3] == "X")or (board[4][4] == "X" and board[4][3] == "X" and  board[4][2] == "X"):
        AI_pos = '5'
        defending = True
    if(board[5][5] == "X" and board[5][4] == "X" )or (board[5][5] == "X" and board[5][4] == "X" and  board[5][3] == "X")or (board[5][4] == "X" and board[5][3] == "X" and  board[5][2] == "X"):
        AI_pos = '6'
        defending = True
    if(board[6][5] == "X" and board[6][4] == "X" )or (board[6][5] == "X" and board[6][4] == "X" and  board[6][3] == "X")or (board[6][4] == "X" and board[6][3] == "X" and  board[6][2] == "X"):
        AI_pos = '7'
        defending = True  
    
    # vertical
    
    for y in range(6):
        x=0
        if (board[x+1][y-1]=='X' and board[x+2][y-1]=='X'and board[x][y-1]==' '):
            if y-1 >=2:     
                if board[x][y]!=' ':
                    AI_pos =  '1'
                    defending = True                    
            else:
                AI_pos =  '1'
                defending = True
        if (board[x+2][y-1]=='X' and board[x+3][y-1]=='X'and board[x+1][y-1]==' '):
            if y-1 >=2:     
                if board[x+1][y]!=' ':
                    AI_pos =  '2'
                    defending = True                    
            else:
                AI_pos =  '2'
                defending = True 
        if (board[x][y-1]=='X' and board[x+1][y-1]=='X'and board[x+2][y-1]==' ') or (board[x+2][y-1]==' ' and board[x+3][y-1]=='X'and board[x+4][y-1]=='X'):
            if y >=2:     
                if board[x+2][y]!=' ':
                    AI_pos =  '3'
                    defending = True                    
            else:
                AI_pos =  '3'
                defending = True 
        if (board[x+1][y]=='X' and board[x+2][y]=='X'and board[x+3][y]==' ')or(board[x+3][y]==' ' and board[x+4][y]=='X'and board[x+5][y]=='X'):
            if y >=2:     
                if board[x+3][y]!=' ':
                    AI_pos =  '4'
                    defending = True 
            else:
                AI_pos =  '4'
                defending = True 
        if (board[x+2][y]=='X' and board[x+3][y]=='X'and board[x+4][y]==' ')or(board[x+4][y]==' ' and board[x+5][y]=='X'and board[x+6][y]=='X'):
            if y >=2:
                if board[x+4][y]!=' ':
                    AI_pos =  '5'
                    defending = True
            else:
                AI_pos =  '5'
                defending = True
        if (board[x+3][y]=='X' and board[x+4][y]=='X'and board[x+5][y]==' '):
            if y >=2:
                if board[x+5][y]!=' ':
                    AI_pos =  '6'
                    defending = True 
            else:
                AI_pos =  '6'
                defending = True 
        if (board[x+4][y]=='X' and board[x+5][y]=='X'and board[x+6][y]==' '):
            if y >=2:
                if board[x+6][y]!=' ':
                    AI_pos =  '7'
                    defending = True 
            else:
                AI_pos =  '7'
                defending = True 
                                  
    if(board[0][4]=='X'and board[1][3]=='X'and board[2][2]=='X'and board[3][1]==' '):
        if (board[3][2]!=' ') :
            AI_pos =  '4'
            defending = True 
    if( board[1][3]=='X'and board[2][2]=='X'and board[3][1]=='X'and  board[4][0]==' '):
        if (board[4][1]!=' ') :
            AI_pos =  '5'
            defending = True 
    
    
    if( board[0][5]=='X'and board[1][4]=='X'and board[2][3]=='X'and  board[3][2]==' '):
        if (board[3][3]!=' ') :
            AI_pos =  '4'
            defending = True 
                                        
    if(board[1][5]=='X'and board[2][4]=='X'and board[3][3]=='X'and board[4][2]==' '):
        if (board[4][3]!=' ') :
            AI_pos =  '5'
            defending = True 
            
    if( board[2][5]=='X'and board[3][4]=='X'and board[4][3]=='X'and  board[5][2]==' '):
        if (board[5][3]!=' ') :
            AI_pos =  '6'
            defending = True 
    if( board[3][4]=='X'and board[4][3]=='X'and  board[5][2]=='X' and board[6][1]==' '):
        if (board[6][2]!=' ') :
            AI_pos =  '7'
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
    for x in range(7):
        y=0
        if (board[x-1][y] == 'O' and board[x-1][y-1] == 'O' and board[x-1][y-2] == 'O' and board[x-1][y-3] == ' '):
            AI_pos =  '1'
            attacking = True
        if (board[x-1][y] == 'O' and board[x-1][y-1] == 'O' and board[x-1][y-2] == 'O' and board[x-1][y-3] == ' '):
            AI_pos =  '2'
            attacking = True
    return attacking, AI_pos
def win (board):
    # horizontal
    for y in range(6):
        winning = []
        for x in range(7):
            if board[x][y] != 'A':
                winning.append([board[x][y]])
        if len(winning) > 3:
            for i in range(5):
                if winning[i-1]==['X'] and winning[i]==['X'] and winning[i+1]==['X'] and winning[i+2]==['X']:
                    return True
                if winning[i-1]==['O'] and winning[i]==['O'] and winning[i+1]==['O'] and winning[i+2]==['O']:
                    return True                   
        else:
            winning = []

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
            winning = []
    
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
                        move = getcommove(mainBoard, computerTile)
                        setMove(mainBoard, computerTile,move)
                        
                if win(mainBoard) == True :
                    break
                turn = 'Your'
                print ("--computer Move--")
                print ('com move --> ',AI_pos)

        setDrawBoard(mainBoard)
        print (turn,' win ')
        break
                
                
                
                
                
