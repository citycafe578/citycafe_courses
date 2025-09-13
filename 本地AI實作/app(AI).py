from funs import draw, check_turn, check_win
from ollama import chat, ChatResponse
import requests
import re
import pyautogui as pg
play = True
turn = 0
game_map = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def ask_AI(game_map):
    response: ChatResponse = chat(model='TinyLlama', messages=[
    {
        'role': 'user',
        'content':f"""
                你是一位井字棋高手，正在與玩家進行對戰。棋盤是一個 3x3 的九宮格，位置編號如下：

                1 | 2 | 3  
                ---------
                4 | 5 | 6  
                ---------
                7 | 8 | 9

                目前的棋盤狀態如下（O 為玩家，X 為你）：
                {game_map}
                你的任務是在玩家使用三個 O 連成一條線前先使用 X 連成一條線
                同時你也可以透過你的 X 阻止玩家達成勝利條件
                請根據目前的局勢，選擇你要下的位置（輸入尚未被選擇的編號，例如 1、5、9）。  
                請只回覆一個數字，不要加上任何說明或標點。
                """,
    },
    ])

    ai_reply = response.message['content'].strip()
    match = re.search(r'\b[1-9]\b',ai_reply)
    if match:
        move = int(match.group(0))
        if game_map[move] not in ['X', 'O']:
            return move

    for i in range(1, 10):
        if game_map[i] not in ['X', 'O']:
            return i
    return ai_reply

while(play):
    draw(game_map)
    human = input()
    if(turn % 2 == 0):
        try:
            
            if human == 'q':
                print("退出遊戲")
                play = False
            elif not human.isdigit() or int(human) < 1 or int(human) > 9:
                print("輸入僅能為數字 1 ~ 9 或是 q")
            elif game_map[int(human)] in ['X', 'O']:
                print("該選項已被選擇")
            else:
                game_map[int(human)] = check_turn(turn)
                pg.press('enter')
                turn += 1
        except ValueError:
            print("請輸入有效的數字或 q")
    else:
        game_map[int(ask_AI(game_map))] = check_turn(turn)
        turn += 1 

    if(check_win(game_map) == True):
        if((turn - 1) % 2 == 0):
            print("遊戲結束，玩家勝利")
        else:
            print("遊戲結束，電腦勝利")  ###
        play = False

    if(turn > 9):
        print("遊戲結束，平手")
        play = False


