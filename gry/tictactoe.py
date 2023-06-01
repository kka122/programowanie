from math import ceil
board=[["1","2","3"],["4","5","6"],["7","8","9"]]
x_move = True



def print_board():
    for row  in board:
        print(row[0],"|",row[1],"|",row[2])


def is_input_valid(a):
    k = ["1","2","3","4","5","6","7","8","9"]
    for i in k:
        if a == i:
            return True
    return False    

def tic_tac_or_toe(a):
    row = ceil(int(a)/3)-1
    col = (int(a)-1)%3 
    return row,col



def main():
    global x_move
    while True:
        print_board()
        a=input("wpisz liczbe na ktorej chcesz postawic kolko albo krzyzyk ")
        if is_input_valid(a):
            print("ok")
            row,col=tic_tac_or_toe(a)
            board[row][col] = "x"
            if x_move:
                x_move = False
            else:
                x_move = True
        else:
            print("nie")
    


main()