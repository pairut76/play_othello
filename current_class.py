#Pairut Dumkuengthanant
#ID: 64856070

class Current():
    #changes state and creates center peices
    def new_board(row, col, color, state)->'new game state':
        if color=='B':
            state[(int(row)//2)][(int(col)//2)]='B'
            state[(int(row)//2)-1][(int(col)//2)-1]='B'
            state[(int(row)//2)-1][(int(col)//2)]='W'
            state[(int(row)//2)][(int(col)//2)-1]='W'
        if color=='W':
            state[(int(row)//2)][(int(col)//2)]='W'
            state[(int(row)//2)-1][(int(col)//2)-1]='W'
            state[(int(row)//2)-1][(int(col)//2)]='B'
            state[(int(row)//2)][(int(col)//2)-1]='B' 
                       
        return state
    
    def new_gstate(row, col, turn, state):
        state[int(row)-1][int(col)-1]=str(turn)
     
        return state
    def flip_color(valid_lst,turn,state):
        for x,y in valid_lst:
            state[x][y]=str(turn)

        return state
    def winner(rule, b, w):
        if str(rule)=='>':
            if int(b)>int(w):
                return 'B'
            if int(w)>int(b):
                return 'W'
        if str(rule)=='<':
            if int(b)<int(w):
                return 'B'
            if int(w)<int(b):
                return 'W'
        else:
            return None
                
