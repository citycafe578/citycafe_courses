import math
import random
import pygame
import threading
import time
import ollama

width = 500
height = 500
cols = 25
rows = 20

# 遊戲規則
game_rules = (
    "你正在玩貪食蛇遊戲。規則如下："
    "1. 蛇每次只能往「上、下、左、右」四個方向移動一步。"
    "2. 蛇不能撞到牆壁或自己的身體，否則遊戲結束。"
    "3. 吃到食物（Food）時，蛇會變長，並在地圖上隨機產生新的食物。"
    "4. 請根據目前蛇頭的位置、方向、身體座標與食物座標，回覆你要移動的方向（'UP'、'DOWN'、'LEFT'、'RIGHT'）。"
    "5. 只需回覆方向，不要加其他說明。"
)

class cube():
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake():
    def __init__(self, color, pos):
        self.body = []
        self.turns = {}
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        # 由AI控制，不再讀取鍵盤
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx,c.dirny)

    def set_direction(self, direction):
        # 依AI回傳方向設定
        if direction == "UP" and self.dirny != 1:
            self.dirnx = 0
            self.dirny = -1
        elif direction == "DOWN" and self.dirny != -1:
            self.dirnx = 0
            self.dirny = 1
        elif direction == "LEFT" and self.dirnx != 1:
            self.dirnx = -1
            self.dirny = 0
        elif direction == "RIGHT" and self.dirnx != -1:
            self.dirnx = 1
            self.dirny = 0
        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def reset(self,pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def redrawWindow():
    global win
    win.fill((0,0,0))
    drawGrid(width, rows, win)
    s.draw(win)
    snack.draw(win)
    pygame.display.update()

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn
        pygame.draw.line(surface, (255,255,255), (x, 0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0, y),(w,y))

def randomSnack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)

def get_game_info():
    # 組合給AI的遊戲資訊
    return f"Head: {s.head.pos}, Dir: ({s.dirnx},{s.dirny}), Length: {len(s.body)}, Body: {[c.pos for c in s.body]}, Food: {snack.pos}"

def ai_thread_func():
    global running
    # 等待 s 和 snack 初始化
    while 's' not in globals() or 'snack' not in globals():
        time.sleep(0.1)
    while running:
        prompt = game_rules + get_game_info()
        response = ollama.chat(
            model="gemma",
            messages=[{"role": "user", "content": prompt}]
        )
        action = response["message"]["content"].strip().upper()
        if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            s.set_direction(action)
        else:
            print("AI 回傳未知指令:", action)
        time.sleep(0.05)

def main():
    global s, snack, win, running
    win = pygame.display.set_mode((width,height))
    s = snake((255,0,0), (10,10))
    s.addCube()
    snack = cube(randomSnack(rows,s), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        headPos = s.head.pos
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
            print("Score:", len(s.body))
            s.reset((10, 10))
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s), color=(0,255,0))
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score:", len(s.body))
                s.reset((10,10))
                break
        redrawWindow()

running = True
game_thread = threading.Thread(target=main)
ai_thread = threading.Thread(target=ai_thread_func)
game_thread.start()
ai_thread.start()