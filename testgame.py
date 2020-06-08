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
run = True


class Player:
    def __init__(self, name, x, y, width, height, health):
        self.height = health
        self.height = height
        self.y = y
        self.x = x
        self.width = width
        self.name = name
        self.vel = 10
        self.jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.doz = False
        self.walk_count = 0

    def charDraw(self):

        if self.walk_count + 1 >= 9:
            self.walk_count = 0
        if self.right:
            window.blit(walkRight[self.walk_count], (self.x, self.y))
            self.walk_count += 1
        elif self.left:
            window.blit(walkLeft[self.walk_count], (self.x, self.y))
            self.walk_count += 1
        else:
            window.blit(char, (self.x, self.y))

        pygame.display.update()


def gameWindow():
    window.blit(bg, (0, 0))
    pygame.display.update()


ratul = Player('Adiat', 0, 410, 64, 64, 100)


while run:
    timeFrame.tick(14)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not ratul.jump:
        if keys[pygame.K_SPACE]:
            ratul.jump = True
    else:
        if ratul.jump_count >= -10:
            ratul.y -= (ratul.jump_count * abs(ratul.jump_count)) * .5
            ratul.jump_count -= 2
        else:
            ratul.jump = False
            ratul.jump_count = 10
    if keys[pygame.K_LEFT] and ratul.x > 0:
        ratul.left = True
        ratul.right = False
        ratul.x -= ratul.vel
    elif keys[pygame.K_RIGHT] and ratul.x < 600 - ratul.width:
        ratul.left = False
        ratul.right = True
        ratul.x += ratul.vel
    elif keys[pygame.K_DOWN]:
        doz = True
    else:
        ratul.left = False
        ratul.right = False
    gameWindow()
    Player.charDraw(ratul)

pygame.quit()
