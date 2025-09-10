from funs import draw, check_turn, check_win
import string
play = True
turn = 0
map = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


while(play):
    draw(map)
    human = input()
    try:
        if human == 'q':
            print("退出遊戲")
            play = False
        elif not human.isdigit() or int(human) < 1 or int(human) > 9:
            print("輸入僅能為數字 1 ~ 9 或是 q")
        elif map[int(human)] in ['X', 'O']:
            print("該選項已被選擇")
        else:
            map[int(human)] = check_turn(turn)
            turn += 1
    except ValueError:
        print("請輸入有效的數字或 q")

    if(check_win(map) == True):
        if((turn - 1) % 2 == 0):
            print("遊戲結束，玩家 1 勝利")
        else:
            print("遊戲結束，玩家 2 勝利")
        play = False

    if(turn > 9):
        print("遊戲結束，平手")
        play = False


    