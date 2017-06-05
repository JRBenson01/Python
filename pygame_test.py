import pygame, sys
from pygame.locals import *
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("A bit Racey")

gameDisplay.fill((255, 255, 0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
        pygame.display.update()
