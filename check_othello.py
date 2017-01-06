#Pairut Dumkuengthanant
#ID: 64856070

#check if move is valid
def valid_move(u_row, u_col, ini_row, ini_col, turn, current_s):
    if int(u_row)<=0:
        return False
    if int(u_col)<=0:
        return False
    if int(u_row)>int(ini_row):
        return False
    if int(u_col)>int(ini_col):
        return False
    if current_s[int(u_row)-1][int(u_col)-1]!='.':
        return False
    lst=(move(u_row,u_col,ini_row, ini_col,current_s,turn))

    if len(lst)==0:
        return False
    else:
        return True

#test the inputs if there are moves available                 
def move(u_row,u_col,ini_row, ini_col,current_s,turn)->'lif of flip':
    vects=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    lst_flip=[]
    for vec in vects:
        range_value=1
        lst1_flip=[]
        while __in_board(u_row,u_col, vec,ini_row,ini_col,range_value):
            
            row=((int(u_row)-1))+(vec[0]*int(range_value))
            col=((int(u_col)-1))+(vec[1]*int(range_value))
            pos=(current_s[row][col])
            
            if (pos)=='.':
                break
            if (pos)==str(turn):
                for item in lst1_flip:
                    lst_flip.append(item) 
                break
     
            else:
                range_value=range_value+1
                lst1_flip.append([row,col])
               
    return lst_flip         

#check if inputs are in the board
def __in_board(u_row,u_col,vec,ini_row, ini_col,rage):
    row=(int(u_row)-1)+vec[0]*int(rage)
    col=(int(u_col)-1)+vec[1]*int(rage)
   
    max_row=int(ini_row)-1
    max_col=int(ini_col)-1
    
    if 0<=row<=(max_row) and 0<=col<=(max_col):
        return True

    else:
        return False

#check for available moves
def check(ini_row, ini_col, ini_state,cur_turn):
    count=0
    
    for i in range(int(ini_row)):
        for k in range(int(ini_col)):
            if valid_move((i+1),(k+1), ini_row, ini_col, cur_turn, ini_state):
                count+=1     
    if count!=0:
        return False
    else:            
        return True
#check for board filled with only one color
def check2(ini_row, ini_col, current_s):
    countb=0
    countw=0
    for i in range(int(ini_row)):
        for k in range(int(ini_col)):
            if current_s[i][k]=='B':
                countb+=1
                
            if current_s[i][k]=='W':
                countw+=1
    if countb==0 or countw==0:
        return True
    else:
        return False
    

    








   
    
            
