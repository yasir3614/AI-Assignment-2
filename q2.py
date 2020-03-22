# USE PYTHON 3.8.x

# Problem: N - queens
#Intialize Board For N Queens
def board_initializer(board,n):
    for i in range(0,n):
        temp_list = []
        for j in range(0,n):
            temp_list.append(0)
        board.append(temp_list)
    return board


#Checks Collisions in lower diagonal
def lowerDiagonal(board, R, C):
    while 1 == 1:
        R+=1
        C-=1
        if (R < (len(board)) and C < (len(board[R]))):
            if board[R][C] == 1:
                    return False
        else:
            break
    return True

#Checks Collisions at Upper Diaogonal
def checkLeftDiagonal(board, R, C):
    while 1 == 1:
        R-=1
        C-=1
        if (R>=0 and R < (len(board)) and C>=0 and C < (len(board[R]))):
            if board[R][C] == 1:
                    return False
        else:
            break
    return True


#Checks collisions in rows or columns
def checkRowCol(board, R, C):
    for i in range(0, C):
        if board[R][i] == 1:
            return False
    return True


#Finds the solution for current valid positions
def isValidPositions(board, R, C):
   
    if not (checkLeftDiagonal(board, R, C)  and checkRowCol(board,R,C) and lowerDiagonal(board, R, C)):
        return False
    return True


#Function to display the Board
def printBoard(board):
    for R in range(0, len(board)):
        print("") 
        for C in range(0, len(board)):
            if(board[R][C] == 1):
                print("Q"," ",end='')
            else:
                print("*"," ",end='')
    return None
            
       
#Solution finding by recursion of board and backtracking
def get_n_queens(board, C):
    if (C  >= len(board)):
        return True
    
   
    for R in range(0,len(board)):
        if (isValidPositions(board,R, C)):
            board[R][C] = 1

            if get_n_queens(board, C+1) == True:
                return True
            
            #Backtracking by reseting the queen value if its not valid
            board[R][C] = 0 
    
    return False

print("Enter the size of N: ")
N = int(input())
board = board_initializer([],N)  
def main():
    get_n_queens(board, 0)
    printBoard(board)
    print("--------------------------------")
if __name__ == "__main__":
    main()