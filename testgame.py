import pygame

pygame.init()

pygame.display.set_caption('PUBG')

window = pygame.display.set_mode((600, 400))


x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_UP]:
    #
    # if keys[pygame.K_DOWN]:
    #
    # if keys[pygame.K_LEFT]:
    #
    # if keys[pygame.K_RIGHT]:

    pygame.draw.rect(window, (255, 9, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()