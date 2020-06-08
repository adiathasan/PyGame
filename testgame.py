import pygame

pygame.init()

pygame.display.set_caption('PUBG')

window = pygame.display.set_mode((600, 400))


x = 50
y = 50
width = 40
height = 50
vel = 10
jump_count = 10
jump = False
run = True
a = 0
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not jump:
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 400 - height:
            y += vel
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
        x -= vel
    if keys[pygame.K_RIGHT] and x < 600 - width:
        x += vel

    window.fill((0, 0, 0))
    a += 11
    try:
        pygame.draw.rect(window, (a, 9, 0), (x, y, width, height))
    except TypeError:
        a = 10
    pygame.display.update()

pygame.quit()
