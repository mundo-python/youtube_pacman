import pygame
from board import boards

pygame.init()

WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = boards

run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()