import random

def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[1])+"   |   "+str(board[2])+"   |   "+str(board[3])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[4])+"   |   "+str(board[5])+"   |   "+str(board[6])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[7])+"   |   "+str(board[8])+"   |   "+str(board[9])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    while(True):
        move=int(input("Enter your move: "))
        if 0<move<10:
            if board[move]!="O" and board[move]!="X":
                board[move]="O"
                return
        
def MakeListOfFreeFields(board):
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    lst=[]
    for values in board:
        if values not in ["O","X"]:
            lst.append(values)
    return lst
    
def VictoryFor(board, sign):
    
    if(board[1]==sign and board[2]==sign and board[3]==sign):
        
        return True
    if(board[4]==sign and board[5]==sign and board[6]==sign):
        
        return True
    if(board[7]==sign and board[8]==sign and board[9]==sign):
        
        return True
    if(board[1]==sign and board[4]==sign and board[7]==sign):
       
        return True
    if(board[2]==sign and board[5]==sign and board[8]==sign):
        
        return True
    if(board[3]==sign and board[6]==sign and board[9]==sign):
        
        return True
    if(board[1]==sign and board[5]==sign and board[9]==sign):
        
        return True
    if(board[3]==sign and board[5]==sign and board[7]==sign):
        return True
    
    
def DrawMove(board):
    while(True):
        comp=random.randrange(1,10)
        if board[comp]!="O" and board[comp]!="X":
            board[comp]="X"
            return
    
board=[value for value in range(10)]
board[5]="X"
DisplayBoard(board)
while(True):
    
    
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board,"O"):
        print("You won!")
        break
    
    if(len(MakeListOfFreeFields(board))==0):
        print("GameOver")
        break
    DrawMove(board)
    DisplayBoard(board)
    if VictoryFor(board,"X"):
        print("Computer won!")
        break
    if(len(MakeListOfFreeFields(board))==1):
        print("GameOver")
        break
    
    