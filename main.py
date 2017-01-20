import pygame
from pygame.locals import *

pygame.init()
gamepad = pygame.display.set_mode((1024,512), DOUBLEBUF)
pygame.display.set_caption('PyGame')

clock = pygame.time.Clock()


crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    gamepad.fill((255,255,255))
    pygame.display.update()
    clock.tick(60)