from __future__ import print_function
import random
def setDrawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+---+'
    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(y+1, end = " ")
        for x in range(8):
            print('| %s' % (board[x][y]), end = " ")
        print('|')
        print(HLINE)
        
def setNewBoard():
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board


def setStartBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    board[4-1][4-1] = 'X'
    board[5-1][4-1] = 'O'
    board[4-1][5-1] = 'O'
    board[5-1][5-1] = 'X'

def checkMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile 
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection 
        y += ydirection 
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): 
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
               
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    board[xstart][ystart] = ' ' 
    if len(tilesToFlip) == 0: 
        return False
    return tilesToFlip

def getAcceptMoves(board, tile):
    AcceptMoves = []
    for x in range(8):
        for y in range(8):
            if checkMove(board, tile, x, y) != False:
                AcceptMoves.append([x, y])
    return AcceptMoves
def getComputerMove(board, computerTile):
    pos_Moves = getAcceptMoves(board, computerTile)
    random.shuffle(pos_Moves)
    for x, y in pos_Moves:
        if isOnCorner(x, y):
            return [x, y]
    bestScore = -1
    for x, y in pos_Moves:
        testBoard = getBoardCopy(board)
        setMove(testBoard, computerTile, x, y)
        score = getScoreOfBoard(testBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}
def setMove(board, tile, xstart, ystart):
    tilesToFlip = checkMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
   
    testBoard = setNewBoard()

    for x in range(8):
        for y in range(8):
            testBoard[x][y] = board[x][y]
    return testBoard
def getYourMove(board, YourTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        move = raw_input('Enter your move <x,y>:')
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if checkMove(board, YourTile, x, y) == False:
                print ("--")
                continue
            else:
                break
        else:
            print('--(1-8)')
    return [x, y]

def isOnBoard(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <=7
def isOnCorner(x, y):
    return (x == 0 and y == 0) or (x == 8 and y == 0) or (x == 0 and y == 8) or (x == 8 and y == 8)

def showPoints(YourTile, computerTile):
    scores = getScoreOfBoard(mainBoard)
    print('You  %s points. computer  %s points.' % (scores[YourTile], scores[computerTile]))
def showEndPointe(YourTile, computerTile):
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[YourTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[YourTile] - scores[computerTile]))
    elif scores[YourTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[YourTile]))
    else:
        print('The game was a tie!')

    
def GoFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'Your'

while True:
   
    mainBoard = setNewBoard()
    setStartBoard(mainBoard)
    YourTile, computerTile = "X","O" 
    turn = GoFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'Your':
            # Your 
            setDrawBoard(mainBoard)
            showPoints(YourTile, computerTile)
            move = getYourMove(mainBoard, YourTile)
            setMove(mainBoard, YourTile, move[0], move[1])
            if getAcceptMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'
        else:
            # Computer 
            setDrawBoard(mainBoard)
            showPoints(YourTile, computerTile)
            x, y = getComputerMove(mainBoard, computerTile)
            setMove(mainBoard, computerTile, x, y)
            if getAcceptMoves(mainBoard, YourTile) == []:
                break 
            else:
                turn = 'Your'
    # Display end
    setDrawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    showEndPointe(YourTile, computerTile)
    break
    
