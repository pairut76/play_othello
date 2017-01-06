#Pairut Dumkuengthanant
#ID: 64856070

#user input
import check_othello
import current_class

#prints current board
def print_board(col, row, state)->None:
    for i in range(int(col)):
        print('\n','    '.join(state[i]))
#prints new board        
def new_board(cols, rows)->'[board]':
    lst=[]
    for row in range(cols):
            lst1=[]
            for col in range(rows):
                lst1.append('.')
            lst.append(lst1)
    return lst
#asks for move valid row and column
def u_row_col(row, col)->'row, column':
    while True:
        move=input(" ")
        if len(move.split(' '))==2:
            u_row, u_col=move.split(' ')
            if u_row!=' ' and u_col!=' ':
                if 1<=int(u_row)<=int(row) and 1<=int(u_col)<=int(col):
                    return u_row, u_col
                else:
                    print('\nINVALID')
            else:
                print('\nINVALID')

        else:
            print('\nINVALID')
#size of board    
def row_col()->'''int(col, row)''':
    while True:
        row = input(" ")
        column = input(" ")
        if (4<=int(row)<=16) and (4<=int(column)<=16):
            if int(row)%2==0 and int(column)%2==0:
                return column, row
            else:
                print('INVALID')
        else:
            print('INVALID')
#who will go first           
def first_move()->'''int(count)''':
    while True:
        turn=input(" ")
        if (turn=='B') or (turn=='W'):
            return turn
        else:
            print('INVALID')
#asks for user input of arrangement of center color
def center_board()->'''color''':
    while True:
        color_center=input(' ')
        if (color_center=='B') or (color_center=='W'):
            return color_center
        else:
            print('INVALID')
#asks for user of the game rule
def game_rule()->'game rule of less than or greater than':
    
    while True:
        rule=input(' ')
        if rule=='>' or rule=='<':
            return rule
        else:
            print('INVALID')
#switches turn
def u_turn(turn):
    if turn=='B':
        return 'W'
    if turn=='W':
        return 'B'
#check the number of pieces of black and white on board    
def check_board(state)->'int(B), int(W)':
    W=0
    B=0
    for i in state:
        for k in i:
            if k=='B':
                B+=1
            if k=='W':
                W+=1
    return W, B
#check for board full
def __check_winner(state,ini_row, ini_col):
    max_num=int(ini_row)*int(ini_col)
    count=0
    
    for i in range(int(ini_row)):
        for k in range(int(ini_col)):
            if state[i][k]=='.':
                count+=1
    if count==0:
        return True
    else:
        return False    
        
def main():
    col,row=row_col()
    turn1=first_move()
    center=center_board()
    rule=game_rule()
    
    initial_state=new_board(int(col), int(row))
  
    current_s=current_class.Current.new_board(row, col, center, initial_state)
    while True:
        
        w, b=check_board(current_s)
        print('B: ',b,'  ','W: ',w)
        print_board(col, row, current_s)
        print('TURN: ', turn1)
        u_row, u_col=u_row_col(row, col)
    
        if (check_othello.valid_move(u_row, u_col, row, col, turn1, current_s)):
    
            lst_va=check_othello.move(u_row,u_col, row, col,current_s, turn1)
            current_s=current_class.Current.flip_color(lst_va,turn1,current_s)
            current_s=current_class.Current.new_gstate(u_row, u_col, turn1, current_s)
            print('\nVALID')
            turn1=u_turn(str(turn1))
       
            if __check_winner(current_s, row, col) or check_othello.check2(row, col, current_s):
                win=current_class.Current.winner(rule,b,w)
                if win==None:
                    print('WINNER: NONE')
                else:
                    print('WINNER: ',win)
                    print_board(col, row, current_s)
            
                break
           
            if check_othello.check(row,col,current_s,turn1):
                turn1=u_turn(str(turn1))
                if check_othello.check(row,col,current_s,turn1):
                    win=current_class.Current.winner(rule,b,w)
                    if win==None:
                        print('WINNER: NONE')
                    else:
                        print('WINNER: ',win)
                        print_board(col, row, current_s)
                    break
     
       
        
  
        else:
            print('\nINVALID')
       
        
                
if __name__=='__main__':
    
    main()
