def draw(map):
    board = (f'|{map[1]}||{map[2]}||{map[3]}| \n'
             f'|{map[4]}||{map[5]}||{map[6]}| \n'
             f'|{map[7]}||{map[8]}||{map[9]}| \n')
    print(board)

def check_turn(trun):
    if(trun % 2 == 0):
        return "O"
    else:
        return "X"
    
def check_win(map):
    if(map[1] == map[2] == map[3] or
       map[4] == map[5] == map[6] or
       map[7] == map[8] == map[9]):
        return True
    elif(map[1] == map[4] == map[7] or
       map[2] == map[5] == map[8] or
       map[3] == map[6] == map[9]):
        return True
    elif(map[1] == map[5] == map[9] or
       map[3] == map[5] == map[7]):
        return True
    else:
        return False
