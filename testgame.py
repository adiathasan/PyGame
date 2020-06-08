import pygame

pygame.init()

pygame.display.set_caption('PUBG')

window = pygame.display.set_mode((600, 470))
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),
             pygame.image.load('R3.png'), pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')

timeFrame = pygame.time.Clock()

char = pygame.image.load('standing.png')


# class Player

x = 0
y = 400
width = 64
height = 64
vel = 10
jump_count = 10
jump = False
run = True
left = False
right = False
doz = False
walk_count = 0
a = 0


def charDraw():
    global walk_count, height, do
    window.blit(bg, (0, 0))
    if walk_count + 1 >= 9:
        walk_count = 0
    if right:
        window.blit(walkRight[walk_count], (x, y))
        walk_count += 1
    elif left:
        window.blit(walkLeft[walk_count], (x, y))
        walk_count += 1
    else:
        window.blit(char, (x, y))

    pygame.display.update()


while run:
    timeFrame.tick(14)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -10:
            y -= (jump_count * abs(jump_count)) * .5
            jump_count -= 2
            print(y)
        else:
            jump = False
            jump_count = 10
    if keys[pygame.K_LEFT] and x > 0:
        left = True
        right = False
        x -= vel
    elif keys[pygame.K_RIGHT] and x < 600 - width:
        left = False
        right = True
        x += vel
    elif keys[pygame.K_DOWN]:
        doz = True
    else:
        left = False
        right = False

    charDraw()

pygame.quit()
