import pygame


pygame.init()
win = pygame.display.set_mode((50, 50))

x = 100
y = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    x = x + 1

    pygame.time.delay(5)
    win = pygame.display.set_mode((x, y))
    fps = pygame.time.Clock()

