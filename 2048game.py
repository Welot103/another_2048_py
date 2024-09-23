# привет! Управление на W A S D
# следующая подсказка на 164 строке


import pygame
import random
pygame.init()

def re_pos_down(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j][0] != 0:
                x = j
                y = i
                try:
                    while True:
                        if y < len(blocks) and blocks[y+1][x][0] == 0:
                            print(blocks[y][x] , '->', blocks[y+1][x])
                            blocks[y+1][x][0] = blocks[y][x][0]
                            blocks[y][x][0] = 0
                            y += 1
                        elif y < len(blocks) and blocks[y+1][x][0] == blocks[y][x][0]:
                            print(blocks[y][x] , '->+', blocks[y+1][x])
                            blocks[y+1][x][0] = blocks[y][x][0]*2
                            blocks[y][x][0] = 0
                            y += 1
                        else:
                            break
                except:
                    pass
    print(blocks)
    return blocks

def re_pos_up(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j][0] != 0:
                x = j
                y = i
                while True:
                    if y >= 1 and blocks[y-1][x][0] == 0:
                        print(blocks[y][x] , '->', blocks[y-1][x])
                        blocks[y-1][x][0] = blocks[y][x][0]
                        blocks[y][x][0] = 0
                        y -= 1
                    elif y >= 1 and blocks[y-1][x][0] == blocks[y][x][0]:
                        print(blocks[y][x] , '->+', blocks[y-1][x])
                        blocks[y-1][x][0] = blocks[y][x][0]*2
                        blocks[y][x][0] = 0
                        y -= 1
                    else:
                        break
    print(blocks)
    return blocks

def re_pos_right(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j][0] != 0:
                x = j
                y = i
                while True:
                    if x < len(blocks[i]) - 1 and blocks[y][x+1][0] == 0:
                        print(blocks[y][x] , '->', blocks[y][x+1])
                        blocks[y][x+1][0] = blocks[y][x][0]
                        blocks[y][x][0] = 0
                        x += 1
                    elif x < len(blocks[i]) - 1 and blocks[y][x+1][0] == blocks[y][x][0]:
                        print(blocks[y][x] , '->+', blocks[y][x+1])
                        blocks[y][x+1][0] = blocks[y][x][0]*2
                        blocks[y][x][0] = 0
                        x += 1
                    else:
                        break
    print(blocks)
    return blocks

def re_pos_left(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j][0] != 0:
                x = j
                y = i
                while True:
                    if x >= 1 and blocks[y][x-1][0] == 0:
                        print(blocks[y][x] , '->', blocks[y][x-1])
                        blocks[y][x-1][0] = blocks[y][x][0]
                        blocks[y][x][0] = 0
                        x -= 1
                    elif x >= 1 and blocks[y][x-1][0] == blocks[y][x][0]:
                        print(blocks[y][x] , '->+', blocks[y][x-1])
                        blocks[y][x-1][0] = blocks[y][x][0]*2
                        blocks[y][x][0] = 0
                        x -= 1
                    else:
                        break
    print(blocks)
    return blocks

def re_color(blocks):
    color_map = {
        2: (155, 0, 0),
        4: (155, 55, 0),
        8: (155, 110, 0),
        16: (155, 165, 0),
        32: (155, 220, 0),
        64: (120, 220, 0),
        128: (85, 220, 0),
        256: (50, 220, 0),
        512: (15, 220, 0),
        1024: (0, 220, 0),
        2048: (255, 255, 0)
    }
    for y in range(len(blocks)):
        for x in range(len(blocks)):
            block_value = blocks[y][x][0]
            if block_value in color_map:
                blocks[y][x][1] = color_map[block_value]
            else:
                blocks[y][x][1] = (255, 255, 255)  # default color for unknown values
    return blocks

def int_0(blocks):
    air = 0
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j][0] == 0:
                air += 1
    return air

def add_random(blocks, add_count):
    for _ in range(add_count):
        while True:
            if int_0(blocks) == 0:
                break
            y = random.randint(0, len(blocks)-1)
            x = random.randint(0, len(blocks)-1)
            if blocks[y][x][0] < 1:
                if random.randint(0, 10) <= 9:
                    blocks[y][x][0] = 2
                    print('add')
                    break
                else:
                    blocks[y][x][0] = 4
                    print('add')
                    break
    return blocks

def set_blocks(x, y):
    blocks = []
    bl = []
    for i in range(y):
        for j in range(x):
            bl.append([0, (255, 255, 255)])
        blocks.append(bl)
        bl = []
    return blocks


run = True
mw = pygame.display.set_mode((800, 800))
tick = pygame.time.Clock()

# здесь вписывай (x на x), например (8, 8) или (4, 4)   (8 на 8), (4 на 4) клеток (размер поля)
blocks = set_blocks(4, 4)


blocks = add_random(blocks, 2)
blocks = re_color(blocks)


#
font = pygame.font.SysFont('Arial', int(120/len(blocks)))
#

win = 0

while run:
    mw.fill((0, 0, 0))
    for y in range(len(blocks)):
        for x in range(len(blocks)):
            pygame.draw.rect(mw, blocks[y][x][1], (x*800/len(blocks), y*800/len(blocks), 800/len(blocks), 800/len(blocks)))
            text = font.render(str(blocks[y][x][0]), True, (255, 255, 255))
            mw.blit(text, (x*800/len(blocks)+800/len(blocks)/2, y*800/len(blocks)+800/len(blocks)/2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                blocks = re_pos_left(blocks)
                blocks = add_random(blocks, 2)
                blocks = re_color(blocks)
            if event.key == pygame.K_d:
                blocks = re_pos_right(blocks)
                blocks = add_random(blocks, 2)
                blocks = re_color(blocks)
            if event.key == pygame.K_w:
                blocks = re_pos_up(blocks)
                blocks = add_random(blocks, 2)
                blocks = re_color(blocks)
            if event.key == pygame.K_s:
                blocks = re_pos_down(blocks)
                blocks = add_random(blocks, 2)
                blocks = re_color(blocks)
    for i in blocks:
        for j in i:
            if j[0] == 2048:
                win = 1
                break
    tick.tick(60)
    pygame.display.update()
if win == 1:
    print("You win!")