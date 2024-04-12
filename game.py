import pygame
from board import boards
from settings import EMPTY, DOT, HORIZONTAL_WALL, VERTIAL_WALL, POWER_PELLET

pygame.init()


WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = boards


def draw_dot(x, y, block_width, block_height, diameter):
    coor_x = x * block_width + (0.5 * block_width) 
    coor_y = y * block_height + (0.5 * block_height)
    center = coor_x, coor_y
    pygame.draw.circle(screen, "white", center, diameter // 2)
    

def draw_board():
    block_height = ((HEIGHT - 50) // 32)
    block_width = (WIDTH // 30)
    for row_idx, row in enumerate(level):
        for col_idx, cell in enumerate(row):
            if cell == DOT:
                draw_dot(col_idx, row_idx, block_width, block_height, diameter=4)
            if cell == POWER_PELLET:
                draw_dot(col_idx, row_idx, block_width, block_height, diameter=10)

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()