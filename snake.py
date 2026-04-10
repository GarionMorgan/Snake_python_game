import pygame, random

#initialize pygame
pygame.init()

#set display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")

#main game loop
running = True
while running:
    #check if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#end game
pygame.quit()